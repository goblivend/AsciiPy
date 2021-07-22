import imageio as imio
import Ascii
import VideoAscii
import AsciiDico
import PIL


video = imio.get_reader(r".\..\Logo_EPITA.mp4")
VideoAscii.VideoToAscii(video,
                        300,
                        r".\Temp\\",
                        r".\..\Logo_EPITA remake.mp4",
                        False, 10, 2,
                        r".\..\fonts\static\RobotoMono-Regular.ttf")





