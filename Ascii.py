import AsciiDico
import random
import imageio as imio
import numpy as np
from PIL import Image

#img.itemset((10,10,2),100) : 0 b, 1 g, 2 r

def Average(img, isGrayScale):
    if img.size == 0 :
        #print(0)
        return 0
    res = None
    if isGrayScale :
        res = GetAverageGrayScale(img)
    else :
        res = GetAverageRGB(img)
    #print(res)
    return res

def FindLetter(average, Arr) :
    for mini, maxi, letter in Arr :
        if (mini <= average and average < maxi) :
            return letter
    #for tuple in Arr :
    #    if (tuple[0] <= average and average < tuple[1]) :
    #        return tuple[2]

def GetAverageGrayScale(img) :
    return np.average(img)

def GetAverageRGB(img) :
    return np.average(np.average(img, axis=2, weights=[21. / 100., 72. / 100.,7. / 100.]))


def ToAscii(img, prevAscii, prevAverage, nbchar, path, inverted, precision, step, propxy = 2, Arr = AsciiDico.ArrBlocNote, width=0, height=0):
    isGrayScale = True
    if not IsGrayScale(img, precision, width=width, height=height):
        # img = ToGrayScale(img)
        isGrayScale = False


    lines = 0
    columns = 0
    dx = int (width / nbchar)
    dy = propxy * dx

    asciiImage = []
    averageImage = []


    j = 0
    while j < height :
        averageImage.append([])
        asciiImage.append('')
        jTo = j + dy
        if jTo >= height:
            jTo = height - 1
        i = 0
        c = 0
        while i < width :
            iTo = i + dx
            if iTo >= width:
                iTo = width - 1
            averageImage[lines].append(Average(img[int(i):int(iTo):step, int(j):int(jTo):step], isGrayScale))
            if inverted:
                averageImage[lines][c] = 255 - averageImage[lines][c]
            

            #if (prevAscii and prevAverage[lines][c] == averageImage[lines][c]):
            #    asciiImage[lines] += prevAscii[lines][c]
            #else :
            asciiImage[lines] += FindLetter(int(averageImage[lines][-1]), Arr)
            c += 1
            i += dx
        lines += 1
        columns = c
        j += dy
    with open(path, 'w') as f :
        print('\n'.join(asciiImage), file=f)
    return (lines, columns, asciiImage, averageImage)



def IsGrayScale(img, precision, width=0, height=0) :
    width, height, _ = img.shape
    for i in range(precision) :
        (x, y) = (random.randrange(width), random.randrange(height))
        if img[x, y][0] != img[x, y][1] or img[x, y][0] != img[x, y][2] :
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
