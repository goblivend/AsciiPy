
ArrBlocNote = [
[0, 5, 'g'],
[6, 12, '@'],
[13, 22, 'Q'],
[23, 30, '&'],
[31, 34, 'B'],
[35, 37, '$'],
[38, 41, '%'],
[42, 46, '8'],
[47, 51, '#'],
[52, 56, 'D'],
[57, 61, 'G'],
[62, 65, 'R'],
[66, 69, 'M'],
[70, 70, 'p'],
[71, 71, 'O'],
[72, 72, '6'],
[73, 73, '9'],
[74, 75, 'b'],
[76, 76, 'm'],
[77, 77, 'H'],
[78, 78, 'E'],
[79, 79, 'd'],
[80, 80, 'q'],
[81, 84, 'e'],
[85, 85, 'P'],
[86, 86, '5'],
[87, 87, 'a'],
[88, 88, '4'],
[89, 89, 'X'],
[90, 90, 'S'],
[91, 92, 'A'],
[93, 94, 'U'],
[95, 96, 'Z'],
[97, 97, 'h'],
[98, 98, '3'],
[99, 100, 'j'],
[101, 104, '2'],
[105, 105, 'w'],
[106, 106, 'o'],
[107, 107, 'K'],
[108, 108, 'f'],
[109, 109, 'V'],
[110, 110, 'k'],
[111, 111, 'C'],
[112, 112, 'I'],
[113, 114, 't'],
[115, 115, 'F'],
[116, 116, '1'],
[117, 117, '}'],
[118, 118, 'y'],
[119, 119, ']'],
[120, 120, 'n'],
[121, 121, '{'],
[122, 123, 'i'],
[124, 124, '['],
[125, 125, 'J'],
[126, 126, 's'],
[127, 127, 'l'],
[128, 131, 'z'],
[132, 135, 'Y'],
[136, 137, '7'],
[138, 139, 'x'],
[140, 143, 'T'],
[144, 144, '?'],
[145, 145, '='],
[146, 146, 'L'],
[147, 147, 'c'],
[148, 151, '+'],
[152, 153, '('],
[154, 157, '('],
[158, 160, 'r'],
[161, 163, 'v'],
[164, 166, 'x'],
[167, 169, '/'],
[170, 172, ';'],
[173, 173, '\\'],
[174, 175, '>'],
[176, 178, '<'],
[179, 182, '!'],
[183, 184, '*'],
[185, 186, '_'],
[187, 190, '^'],
[191, 193, '"'],
[194, 202, ','],
[203, 213, ':'],
[214, 218, '-'],
[219, 225, '\''],
[226, 231, '.'],
[232, 246, '`'],
[247, 255, ' '],
]

ArrRobotoMono = [
[0, 15, ' '],
[15, 19, '\''],
[19, 30, '.'],
[30, 34, ','],
[34, 38, '-'],
[38, 41, ':'],
[41, 49, '_'],
[49, 64, "'"],
[64, 68, '~'],
[68, 71, '!'],
[71, 79, '^'],
[79, 83, '/'],
[83, 86, '<'],
[86, 90, '='],
[90, 98, 'r'],
[98, 101, '1'],
[101, 105, '('],
[105, 109, '+'],
[109, 116, '?'],
[116, 120, 'L'],
[120, 124, '7'],
[124, 128, 'T'],
[128, 131, 'x'],
[131, 135, 'Y'],
[135, 139, 'f'],
[139, 143, 'l'],
[143, 146, 's'],
[146, 150, 'F'],
[150, 154, 'I'],
[154, 158, 'V'],
[158, 161, 'C'],
[161, 165, '2'],
[165, 169, '%'],
[169, 173, '4'],
[173, 176, 'U'],
[176, 180, '5'],
[180, 184, 'E'],
[184, 188, 'H'],
[188, 191, 'G'],
[191, 195, '#'],
[195, 199, 'g'],
[199, 203, '$'],
[203, 206, '8'],
[206, 218, 'Q'],
[218, 218, '&'],
[218, 225, '0'],
[225, 229, 'B'],
[229, 236, 'N'],
[236, 255, 'M'],
[255, 256, 'W'],
]

import os
import os.path
import imageio as imio
import numpy as np
import Ascii
from PIL import Image, ImageFont, ImageDraw

def GetDicoImg(fontpath, file, lines) :
    file = open(file, "r")
    print(file.name)
    s = file.readlines()

    imageFont = ImageFont.truetype(fontpath, 25)
    height = 31*lines
    img = Image.new('RGB', (15, height), color='black')
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), "".join(s), (255, 255, 255), font=imageFont)

    return (img, height)

def Tryimg(fontpath):
    img = Image.new('RGB', (72, 135), color = 'black')
    draw = ImageDraw.Draw(img)
    imageFont = ImageFont.truetype(fontpath, 60)
    draw.text((0, 0), 'XX\nXX', (255, 255, 255), font=imageFont)
    img.show()


# width = height/2
# 25 => (15, 31)
# 30 => (17.5, 35)
# 60 => (36, 67.5)

# scale = height + 5 = 2 * width + 5

def GetDico(img, lines, height) :
    pixels = img.load()
    for i in range(lines) :
        y= i*31
        yTo = y + 31
        print("\'" + str(chr(i+32)) + "\'," +  str(int(Ascii.Average(img, 0, y, 15, yTo, 1, True))))
        pixels[0, y] = (255, 0, 0)
    img.show()



def GetAnotherDico(lines, fontpath) :
    for i in range(lines):
        img = Image.new('RGB', (15, 31), color='black')
        draw = ImageDraw.Draw(img)
        imageFont = ImageFont.truetype(fontpath, 25)
        draw.text((0, 0), chr(i+32), (255, 255, 255), font=imageFont)
        print("\'" + str(chr(i + 32)) + "\'," + str(int(Ascii.Average(img, 0, 0, 15, 31, 1, True))))
        img.show()

def GetFinal(path) :
    file = open(path, "r")
    print(file.name)
    s = file.readlines()
    for line in s :
        tuple = line.split(';')
        min = tuple[0]
        max = tuple[1]
        char = tuple[2]
        print("[{}, {}, {}],".format(min, max, char))
