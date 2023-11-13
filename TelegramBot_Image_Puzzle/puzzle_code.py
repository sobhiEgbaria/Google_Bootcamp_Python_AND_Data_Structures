from PIL import Image


def puzzle():
    im = Image.open("python.png")

    print(im.size, im.mode, im.format)
