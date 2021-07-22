from AsciiDico import MyArr
import random
import imageio as imio

#img.itemset((10,10,2),100) : 0 b, 1 g, 2 r

def pprint(name) :
    print(name)


def Average(img, x, y, xTo, yTo, step):
    PixelNumber = 0
    PixelSum = 0

    for i in range(x, xTo+1, step):
        for j in range(y, yTo+1, step):
            PixelNumber += 1
            PixelSum += img[j, i, 0]
    return PixelSum / PixelNumber

def FindLetter(average) :
    for tuple in MyArr :
        if (tuple[0] <= average and average <= tuple[1]) :
            return tuple[2]


def ToAscii(img, nbchar, path, inverted, precision, step, propxy = 2):
    if not IsGrayScale(img, precision):
        img = ToGrayScale(img)

    width, height, channels = img.shape
    lines = 0
    columns = 0
    file = open(path, "w")
    dx = int (height / nbchar)
    dy = propxy * dx
    i = 0
    while i < width :
        lines += 1
        iTo = i + dy
        if iTo >= width:
            iTo = width - 1
        j = 0
        c = 0
        while j < height :
            c += 1
            jTo = j + dx
            if jTo >= height:
                jTo = height - 1
            average = Average(img, int(j), int(i), int(jTo), int(iTo), step)
            if inverted:
                average = 255 - average
            file.write(FindLetter(int(average)))
            j += dx
        columns = c
        file.write("\n")
        i += dy
    file.close()
    return (lines, columns)



def IsGrayScale(img, precision) :
    width, height, channels = img.shape
    for i in range(precision) :
        (x, y) = (random.randrange(width), random.randrange(height))
        if img[x, y, 0] != img[x, y, 1] or img[x, y, 0] != img[x, y, 2] :
            return False
    return True


def ToGrayScale(img):
    width, height, channels = img.shape
    for x in range(width):
        for y in range(height):
            r = img[x, y, 0]
            g = img[x, y, 1]
            b = img[x, y, 2]
            average = (21 * r) / 100 + (72 * g) / 100 + (7 * b) / 100

            img.itemset((x, y, 0), average)
            img.itemset((x, y, 1), average)
            img.itemset((x, y, 2), average)
    return img