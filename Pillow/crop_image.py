from PIL import Image

im = Image.open("hopper.ppm")

box = (0, 0, 64, 64)
region = im.crop(box)

region.save("cropped_hopper.png")