import os
import os.path
import imageio as imio
import numpy as np
import Ascii
from PIL import Image, ImageFont, ImageDraw


def VideoToAscii(video, nbchar, tempFolder, finalpath, inversed, precision, step, fontpath):

    (lines, columns) = GetMyFrames(video, nbchar, tempFolder, inversed, precision, step)


    (width, height) = video.get_meta_data()['size']
    fps = video.get_meta_data()['fps']
    # print(f"GetMyVideo(\"{tempFolder}\", \"{finalpath}\", {width}, {height}, {fps}, {lines}, {columns}, \"{fontpath}\")")
    GetMyVideo(tempFolder, finalpath, width, height, fps, lines, columns, fontpath)




def GetMyFrames(video, nbchar, tempFolder, inverted, precision, step):
    count = 0
    (lines, columns) = (0, 0)
    for i, img in enumerate(video):
        (lines, columns) = Ascii.ToAscii(img, nbchar, tempFolder + "img " + str(count) + ".txt", inverted, precision, step, 2)
        count += 1
        print((lines, columns), count)


    return (lines, columns)




def GetMyVideo(tempFolder, finalPath, width, height, fps, lines, columns, font):
    print("test")
    fileList = []
    for (dirpath, dirnames, filenames) in os.walk(tempFolder):
        fileList.extend(filenames)
        break
    print(fileList)

    basicLetterHeight = 25
    scale = height/lines / basicLetterHeight
    fontColor = (255, 255, 255)

    video = imio.get_writer(finalPath, fps=fps)
    for i in range(len(fileList)):
        img = GetAPillowImage(tempFolder + f"img {i}.txt", height, width, 10, font, fontColor, basicLetterHeight, lines)
        video.append_data(img)



def GetAPillowImage(imagename, height, width, scale, fontPath, fontColor, basicLetterHeight, lines):
    img_cv = np.zeros((height, width, 3), np.uint8)
    img_pl = Image.fromarray(img_cv)
    draw = ImageDraw.Draw(img_pl)

    file = open(imagename, "r")
    print(file.name)
    s = file.readlines()

    imageFont = ImageFont.truetype(fontPath, scale)

    # bottomLeftCornerOfText = (0, 0)

    draw.text((0, 0), ConcatenateLines(s), fontColor, font=imageFont)

    return np.array(img_pl)

def ConcatenateLines(lines) :
    s = ""
    for l in lines :
        s += l
    return s


def tryimg(imagename, height, width, scale, fontPath, fontColor):
    img_cv = np.zeros((height, width, 3), np.uint8)
    img_pl = Image.fromarray(img_cv)
    draw = ImageDraw.Draw(img_pl)


    imageFont = ImageFont.truetype(fontPath, scale)

    bottomLeftCornerOfText = (0, 0) # int(line * scale * basicLetterHeight)

    file = open(imagename, "r")
    s = file.readlines()

    draw.text(bottomLeftCornerOfText, ConcatenateLines(s), fontColor, font=imageFont)

    return np.array(img_pl)

