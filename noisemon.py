import csv
import ST7735
import time
from PIL import Image, ImageDraw
from enviroplus.noise import Noise

noise = Noise()

disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=12,
    rotation=90)

disp.begin()

img = Image.new('RGB', (disp.width, disp.height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

while True:
    amps = noise.get_amplitudes_at_frequency_ranges([
        (40, 200),
        (201, 500),
        (501, 1000)
    ])
    amps = [n * 32 for n in amps]
    img2 = img.copy()
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    img.paste(img2, (1, 0))
    draw.line((0, 0, 0, amps[0]), fill=(0, 0, 255))
    draw.line((0, 0, 0, amps[1]), fill=(0, 255, 0))
    draw.line((0, 0, 0, amps[2]), fill=(255, 0, 0))

    disp.display(img)

    fields=[amps[0],amps[1],amps[2],time.time()]
    with open(r'nDB.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    time.sleep(.5)