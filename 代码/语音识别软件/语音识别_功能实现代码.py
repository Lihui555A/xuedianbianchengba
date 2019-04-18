from 代码.语音识别软件.语音识别 import Ui_Form
from PyQt5.Qt import *
import sys
from aip import AipSpeech
from pyaudio import PyAudio,paInt16
import wave
import webbrowser
import urllib.request
import json
import pycurl
from PyQt5.Qt import pyqtSignal
from datetime import datetime
import threading
import os

#音频 ：只人能听到的声音在20赫兹到20000赫兹之间的声波，称为音频
#采样频率：指的是每秒取得声音样本的次数，采样频率越高，声音质量越好， 22050是常用的，44100是cd音频
#超过48000或96000采样对人耳已经没有意义，和电影的每秒24帧图片差不多
#如果是双声道采样就是双份的
#采样位数：相当于声音的分辨率，数值越大，越好2字节的就够用了，可以细分到65536个数，已经是cdbi标准了
#通道数：说白了就是几个喇叭发声
#帧：记录了一个声音单元，数值为 采样位数乘通道数
#周期：音频设备一次处理需要的帧数，对于音频设备等的数据访问以及音频数据的储存，都是依次为单位
##交错模式：数字音频信号存储的方式，数据以连续帧的方式存放，即首先记录帧1的左声道样本和右声道样本，再开始帧2的记录
#非交错模式：首先记录的是是一个周期内的所有帧的左声道样本，再记录所有右声道样本
#比特率：每秒的传输速度，
# Aparse.quote(str(voice['result'])[2:-3]), new=2, autoraise=True)PP_ID=16006081
# API_KEY='WEbso2RujRTCvFuQWKCUbN0z'
# SECRET_KEY = 'YWndoDWlfqKAyGyFbY7ZjGEYMIEwQtxR'
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#
class Signal (QObject):
    recognize_result=pyqtSignal(str)   #今天又学会了一招，想在别的普通函数中用信号传递参数，首先要先弄一个类，继承自QObject
    rest_time_singal=pyqtSignal(int)                                   #为什么要写类呢，因为信号都是类的属性，而且记着必须要继承自QObject别的不行，会报错
                                       #这个类定义好了之后呢就可以写信号了记得写信号传递参数的形式，写多少个信号无所谓，关键是咋的用
                                       # 在包含有你自己写的方法的文件中实例化一个刚才我们定义的继承自QObject类的对象，
                                       #然后呢，找到你想发射信号的那个函数，在函数的第一行声明一下刚才的 全局变量，就是在第一行写
                                       #global 刚才定义的对象名       然后想发射啥信号就可以直接用对象名.信号名.emit（实参）
                                       #如果你的信号的实参和形参没啥问题，这个函数一旦运行，那么信号就会被发射  信号的发射算是完事了
                                       #接下来写  怎么接信号
                                       #在包含你想用传递的参数的这个文件中导入刚才的实力化的对象，然后在界面的初始化的类中写上
                                       #对象名.信号名.connect(要连接的槽函数的名称，记着只是函数名称，不用带括号)      槽函数在定义时记得写合适的形参，因为刚才
                                       #信号传递过来是有实参在里面的
                                       #第二种方法
                                       #定义类继承自QQbject
                                       #在类中写信号名称和形参
                                       #在传参文件中定义全局变量，包含实力化一个刚才定义的类，实例化所有的信号，可以用a,b，c 等等来表示一个个的信号
                                       #在传参函数中声明全局变量  就是   global 刚才定义的你想用的信号
                                       # 在函数中写  信号名称.emit(实参)
                                       #在想用这些参数的文件中导入刚才定义的信号名称
                                       #在初始化的时候，或者说全局上定义每个信号要连接的槽函数
                                       #定义槽函数，记得把参数整对。包含类型，顺序，个数

framerate=8000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2
signal=Signal()
a=signal.recognize_result

def save_wave_file(filename,data): #把录得东西写进文件
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()






def my_record(write_time):    #打开录音设备
    global signal
    pa=PyAudio()
    stream = pa.open(format=paInt16, channels=1, rate=framerate, input=True, frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0

    while count < write_time:
        string_audio_data=stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        rest_time = write_time-count
        signal.rest_time_singal.emit(rest_time)
        print('.')    #从这往上都是录音
    save_wave_file('01.wav',my_buf) #这里是吧录得东西写进文件
    stream.close()  #把数据流关闭

def dump_res(buf):
    global a
    print(buf) #buf 返回的是json字节流
    my_temp=json.loads(buf)   #用json给翻译过来
    if my_temp['err_no']:
        if my_temp['err_no']==3301:
            a.emit('说的不清楚，没法识别')
        elif my_temp['err_no']==3300:
            a.emit('参数输错了')
        elif my_temp['err_no']==3302:
            a.emit('账号密码有错误，上不了我的服务器')
        elif my_temp['err_no']==3303:
            a.emit('是我服务器的问题，我不行了，找工程师救我吧')
        elif my_temp['err_no']==3304:
            a.emit('你这弄得时间也太长了吧，我这没法一下处理这么长的数据量')
        elif my_temp['err_no']==3305:
            a.emit('此处超限了，还没玩够？')
    else:
        my_list=my_temp['result'] #拿出我们想要的结果
        print(type(my_list))
        print(my_list[0])
        a.emit(my_list[0])


def get_token():  #这个函数是用来获取云端服务器钥匙的
    apikey='WEbso2RujRTCvFuQWKCUbN0z'
    secretkey='YWndoDWlfqKAyGyFbY7ZjGEYMIEwQtxR'
    auth_url='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+apikey+'&client_secret='+secretkey
    res=urllib.request.urlopen(auth_url)
    json_data=res.read()
    print(json_data,type(json_data))
    print(json.loads(json_data)['access_token'])
    return json.loads(json_data)['access_token']
def use_cloud(token): #拿上钥匙去开始使用服务
    fp=wave.open(u'01.wav','rb')
    nf=fp.getnframes()
    print('sampwidth',fp.getsampwidth())
    print('framrate',fp.getframerate())
    print('channel',fp.getnchannels())
    f_len=nf*2
    audio_data=fp.readframes(nf)
    cuid='xxxxxxxx'
    srv_url='http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token
    http_header=['Content-Type:audio/pcm; rate=8000',
                 'Content-Length:%d'%(f_len)]
    c=pycurl.Curl()
    c.setopt(pycurl.URL,str(srv_url))
    c.setopt(c.HTTPHEADER,http_header)
    c.setopt(c.POST,1)
    c.setopt(c.CONNECTTIMEOUT,80)
    c.setopt(c.TIMEOUT,80)
    c.setopt(c.WRITEFUNCTION,dump_res)   #dump_res 是返回数据的处理函数
    c.setopt(c.POSTFIELDS,audio_data)
    c.setopt(c.POSTFIELDSIZE,f_len)
    c.perform()
def run(write_time):
    my_record(write_time)#这个函数是用来录音的
    print('over')
    use_cloud(get_token())#这个是用来使用云端服务器的
    print('ok')

if __name__ == '__main__':
    write_time=80
    run(write_time)




# import pyaudio
# import wave
# chunk=1024
# wf=wave.open(r'01.wav','rb')
# p=pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
# while True:
#     data=wf.readframes(chunk)
#     if data=='':
#         break
#     stream.write(data)
# stream.close()
# p.terminate()       播放声音











# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
# stream.stop_stream()
# stream.close()
# p.terminate()

#
#
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()# 识别本地文件
# client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {    'lan': 'zh',
# })
# webbrowser.open('https://baidu.com/s?wd=' + urllib.

