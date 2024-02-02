# @author: Sawyer
# @date: 2024/02/02
# @description: 用中文汉字填充，实现彩色字符画

from PIL import Image, ImageDraw, ImageFont

def char_draw(txt:str, image_in:str, image_out:str, font_size:int=10, 
              font:str='simsun.ttc', scale:float=1.0) -> None:
    """
    用中文汉字填充，实现彩色字符画
    @param txt: 填充字符串
    @param image_in: 输入图片路径
    @param image_out: 输出图片路径
    @param font_size: 字体大小
    @param font: 字体名称
    @param scale: 字体缩放比例
    """
    font_size = int(font_size * scale)
    try:
        font = ImageFont.truetype(font, font_size)
    except Exception as e:
        print('Load font error: %s' % e)
        font = ImageFont.truetype('simsun.ttc', font_size)
    im = Image.open(image_in)
    width, height = im.size 
    newImg = Image.new("RGBA", (width, height), (10, 10, 10))   # 背景色
    x = 0
    for i in range(0, height, font_size):
        for j in range(0, width, font_size):
            draw = ImageDraw.Draw(newImg)
            draw.text((j, i), txt[x % len(txt)], fill=im.getpixel((j, i)), font=font)
            x += 1
            del draw
    newImg.save(image_out, 'PNG')


if __name__ == '__main__':
    char_draw(txt='童话', 
              image_in='C:\\Users\\Sawyer\\Desktop\\121.jpg', 
              image_out='C:\\Users\\Sawyer\\Desktop\\test.png', 
              scale=2)