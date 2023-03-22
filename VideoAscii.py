import os
import os.path
import imageio as imio
import numpy as np
import Ascii
import AsciiDico
from PIL import Image, ImageFont, ImageDraw


def VideoToAscii(video, nbchar, tempFolder, finalpath, inversed, precision, step, fontpath, backColor):
                    # (91, 0)
    (lines, columns) = GetMyFrames(video, nbchar, tempFolder, inversed, precision, step)


    (width, height) = video.get_meta_data()['size']
    fps = video.get_meta_data()['fps']
    # print(f"GetMyVideo(\"{tempFolder}\", \"{finalpath}\", {width}, {height}, {fps}, {lines}, {columns}, \"{fontpath}\")")
    GetMyVideo(tempFolder, finalpath, width, height, fps, lines, columns, fontpath, backColor)




def GetMyFrames(video, nbchar, tempFolder, inverted, precision, step):
    count = 0
    (lines, columns) = (0, 0)
    for i, img in enumerate(video):
        img = Image.fromarray(img)
        (lines, columns) = Ascii.ToAscii(img, nbchar, tempFolder + "img " + str(count) + ".txt", inverted, precision, step, 2, Arr= AsciiDico.ArrRobotoMono)
        count += 1
        print((lines, columns), count)


    return (lines, columns)




def GetMyVideo(tempFolder, finalPath, width, height, fps, lines, columns, font, backColor):
    fileList = []
    for (dirpath, dirnames, filenames) in os.walk(tempFolder):
        fileList.extend(filenames)
        break
    print(fileList)
    scale = int(height/lines - 5)
    fontColor = (255, 255, 255)
    img = np.zeros((height, width, 3), np.uint8)
    FillBackGround(img, backColor, width, height)
    #print(np.zeros((width, height, 3), np.uint8))
    video = imio.get_writer(finalPath, fps=fps)
    for i in range(len(fileList)):
        frame = GetAPillowImage(tempFolder + f"img {i}.txt", scale, font, fontColor, img.copy())
        video.append_data(frame)

def FillBackGround(img, color, width, height) :
    for i in range(width) :
        for j in range(height) :
            img[j, i] = color


def GetAPillowImage(imagename, scale, fontPath, fontColor, img):
    img_pl = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pl)

    file = open(imagename, "r")
    print(file.name)
    s = file.readlines()

    imageFont = ImageFont.truetype(fontPath, scale)

    # bottomLeftCornerOfText = (0, 0)

    draw.text((0, 0), "".join(s), fontColor, font=imageFont)

    return np.array(img_pl)


def tryimg(imagename, height, width, scale, fontPath, fontColor):
    img_cv = np.zeros((height, width, 3), np.uint8)
    img_pl = Image.fromarray(img_cv)
    draw = ImageDraw.Draw(img_pl)


    imageFont = ImageFont.truetype(fontPath, scale)

    bottomLeftCornerOfText = (0, 0) # int(line * scale * basicLetterHeight)

    file = open(imagename, "r")
    s = file.readlines()

    draw.text(bottomLeftCornerOfText, "".join(s), fontColor, font=imageFont)

    return np.array(img_pl)

