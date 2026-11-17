from PIL import Image

im = Image.open("hopper.ppm")

box = (0, 0, 64, 64)
region = im.crop(box)

region = region.transpose(Image.Transpose.ROTATE_180)

im.paste(region, box)

im.save("pasted_hopper.png")