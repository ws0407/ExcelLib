# 彩色字符画

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

txt = '童话'    # 填充的汉字
font_size = 20  # 字体的大小
font = ImageFont.truetype('simsun.ttc',font_size)       # 设置字体
im = Image.open('C:\\Users\\Sawyer\\Desktop\\1.jpg')
width, height = im.size 
newImg = Image.new("RGBA", (width, height), (10, 10, 10))   # 背景色
x = 0
for i in range(0, height, font_size):
    for j in range(0, width, font_size):
        draw = ImageDraw.Draw(newImg)
        draw.text((j, i), txt[x % len(txt)], fill=im.getpixel((j, i)), font=font)
        x += 1
        del draw
newImg.save('C:\\Users\\Sawyer\\Desktop\\1.png','PNG')
