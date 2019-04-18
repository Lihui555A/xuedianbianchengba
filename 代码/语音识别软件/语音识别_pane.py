
from 代码.语音识别软件.语音识别 import Ui_Form
from 代码.语音识别软件.语音识别_功能实现代码 import *
from PyQt5.Qt import *
import sys
import urllib.request
import json
import pycurl
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.framerate = 8000
        self.NUM_SAMPLES = 2000
        self.channels = 1
        self.sampwidth = 2

        self.write_time=40

    def voice_reconize(self):
        write_time=10
        self.my_record(write_time)  # 这个函数是用来录音的
        print('over')
        self.use_cloud(self.get_token())  # 这个是用来使用云端服务器的
        print('ok')


    def save_wave_file(self,filename,data): #把录得东西写进文件
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b''.join(data))
        wf.close()

    def my_record(self):  # 打开录音设备
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.framerate, input=True, frames_per_buffer=self.NUM_SAMPLES)
        my_buf = []
        count = 0
        while count < self.write_time:
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1

            print('.')  # 从这往上都是录音
        self.save_wave_file('01.wav', my_buf)  # 这里是吧录得东西写进文件
        stream.close()  # 把数据流关闭

    def get_token(self):  # 这个函数是用来获取云端服务器钥匙的
        apikey = 'WEbso2RujRTCvFuQWKCUbN0z'
        secretkey = 'YWndoDWlfqKAyGyFbY7ZjGEYMIEwQtxR'
        auth_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + apikey + '&client_secret=' + secretkey
        res = urllib.request.urlopen(auth_url)
        json_data = res.read()
        print(json_data, type(json_data))
        print(json.loads(json_data)['access_token'])
        return json.loads(json_data)['access_token']

    def dump_res(self,buf):
        print(buf)  # buf 返回的是json字节流
        my_temp = json.loads(buf)  # 用json给翻译过来
        if my_temp['err_no']:
            if my_temp['err_no'] == 3301:
                self.textBrowser.setText('说的不清楚，没法识别')
            elif my_temp['err_no'] == 3300:
                a.emit('参数输错了')
            elif my_temp['err_no'] == 3302:
                a.emit('账号密码有错误，上不了我的服务器')
            elif my_temp['err_no'] == 3303:
                a.emit('是我服务器的问题，我不行了，找工程师救我吧')
            elif my_temp['err_no'] == 3304:
                a.emit('你这弄得时间也太长了吧，我这没法一下处理这么长的数据量')
            elif my_temp['err_no'] == 3305:
                a.emit('此处超限了，还没玩够？')
        else:
            my_list = my_temp['result']  # 拿出我们想要的结果
            print(type(my_list))
            print(my_list[0])
            a.emit(my_list[0])


    def use_cloud(self,token):  # 拿上钥匙去开始使用服务
        fp = wave.open(u'01.wav', 'rb')
        nf = fp.getnframes()
        print('sampwidth', fp.getsampwidth())
        print('framrate', fp.getframerate())
        print('channel', fp.getnchannels())
        f_len = nf * 2
        audio_data = fp.readframes(nf)
        cuid = 'xxxxxxxx'
        srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
        http_header = ['Content-Type:audio/pcm; rate=8000',
                       'Content-Length:%d' % (f_len)]
        c = pycurl.Curl()
        c.setopt(pycurl.URL, str(srv_url))
        c.setopt(c.HTTPHEADER, http_header)
        c.setopt(c.POST, 1)
        c.setopt(c.CONNECTTIMEOUT, 80)
        c.setopt(c.TIMEOUT, 80)
        c.setopt(c.WRITEFUNCTION, self.dump_res)  # dump_res 是返回数据的处理函数
        c.setopt(c.POSTFIELDS, audio_data)
        c.setopt(c.POSTFIELDSIZE, f_len)
        c.perform()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
