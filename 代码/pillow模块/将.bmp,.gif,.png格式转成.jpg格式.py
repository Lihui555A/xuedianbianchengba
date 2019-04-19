from PIL import Image
import os
def transform(path):
    if type(path)==str and path.endswith(('.bmp','.gif','.png')):
        with Image.open(path) as im:
            im.convert('RGB').save(path[:-3]+'jpg')
#transform(r'C:\Users\36554\Pictures\Camera Roll\1.png')



#批量的图片转格式
def mutitrans(file):
    list=os.listdir(file)
    for filename in list:
        transform(os.path.join(file,filename))
mutitrans(r'C:\Users\36554\Pictures\Camera Roll')