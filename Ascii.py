import AsciiDico
import random
import imageio as imio
from PIL import Image

#img.itemset((10,10,2),100) : 0 b, 1 g, 2 r

def pprint(name) :
    print(name)


def Average(img, x, y, xTo, yTo, step, isGrayScale):
    myFunc = None
    if isGrayScale :
        myFunc = GetAverageGrayScale
    else :
        myFunc = GetAverageRGB

    PixelNumber = 0
    PixelSum = 0

    for i in range(x, xTo, step):
        for j in range(y, yTo, step):
            PixelNumber += 1
            PixelSum += myFunc(img, i, j)
    return PixelSum / PixelNumber

def FindLetter(average, Arr) :
    for tuple in Arr :
        if (tuple[0] <= average and average < tuple[1]) :
            return tuple[2]

def GetAverageGrayScale(img, i, j) :
    p = img.getpixel((i, j))
    if type(p) == int:
        p = (p, p, p)
    r, g, b  = p

    return r

def GetAverageRGB(img, i, j) :
    p = img.getpixel((i, j))
    if type(p) == int:
        p = (p, p, p)

    r = p[0]
    g = p[1]
    b = p[2]

    #r = img[j, i, 0]
    #g = img[j, i, 1]
    #b = img[j, i, 2]
    return (21 * r) / 100 + (72 * g) / 100 + (7 * b) / 100


def ToAscii(img, nbchar, path, inverted, precision, step, propxy = 2, Arr = AsciiDico.ArrBlocNote):
    isGrayScale = True
    if not IsGrayScale(img, precision):
        # img = ToGrayScale(img)
        isGrayScale = False

    width, height = img.size
    lines = 0
    columns = 0
    file = open(path, "w")
    dx = int (width / nbchar)
    dy = propxy * dx
    j = 0
    while j < height :
        lines += 1
        jTo = j + dy
        if jTo >= height:
            jTo = height - 1
        i = 0
        c = 0
        while i < width :
            c += 1
            iTo = i + dx
            if iTo >= width:
                iTo = width - 1
            average = Average(img, int(i), int(j), int(iTo), int(jTo), step, isGrayScale)
            if inverted:
                average = 255 - average
            file.write(FindLetter(int(average), Arr))
            i += dx
        columns = c
        file.write("\n")
        j += dy
    file.close()
    return (lines, columns)



def IsGrayScale(img, precision) :
    width, height = img.size
    draw = img.load()
    for i in range(precision) :
        (x, y) = (random.randrange(width), random.randrange(height))
        if draw[x, y][0] != draw[x, y][1] or draw[x, y][0] != draw[x, y][2] :
            return False
    return True


def ToGrayScale(img):
    width, height = img.size
    draw = img.load()
    for x in range(width):
        for y in range(height):
            r = draw[x, y][0]
            g = draw[x, y][1]
            b = draw[x, y][2]
            average = (21 * r) / 100 + (72 * g) / 100 + (7 * b) / 100

            # img[x, y] = (average, average, average, 255)

            draw[x, y] = (int(average), int(average), int(average))
            # draw.itemset((x, y, 0), average)
            # draw.itemset((x, y, 1), average)
            # draw.itemset((x, y, 2), average)
    return img