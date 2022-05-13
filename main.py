import imageio as imio
import Ascii
import VideoAscii
from AsciiDico import GetDico, Tryimg, GetDicoImg, GetAnotherDico, GetFinal
import AsciiDico
from PIL import Image, ImageFont, ImageDraw
import numpy as np


"""video = imio.get_reader(r".\..\Logo_EPITA.mp4")
VideoAscii.VideoToAscii(video,
                        300,
                        r".\Temp\\",
                        r".\..\Logo_EPITA remake.mp4",
                        True, 10, 2,
                        r".\RobotoMono-Regular.ttf",
                        (30, 30, 30))"""

(width, height) =  (1920, 1080)
(lines, cols) = 90, 321
scale = 10##int(height/lines - 5)
print(scale)
img = np.zeros((height, width, 3), np.uint8)

image = VideoAscii.GetAPillowImage(r".\Temp\img 153.txt", scale, r".\RobotoMono-Regular.ttf", (255, 255, 255), img)
Image.fromarray(image).show()


# img = Ascii.ToAscii(img, 200, r".\..\Image 52bk.txt", False, 5, 1)
# imio.imwrite(r".\..\Image 52bk.png", img)


"""

def GetBackGround2(width, height, color):
    img = np.zeros((width, height, 3), np.uint8)
    img = Image.fromarray(img)
    test = img.load()
    for i in range(width) :
        for j in range(height) :
            test[i, j] = color
    img.save(r".\..\Image 99bk2.png")

color = (69, 42, 7)
GetBackGround2(1000, 1000, color)"""

