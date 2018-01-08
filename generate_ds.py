from PIL import Image, ImageDraw
import random
import pandas as pd
import os
import shutil

IMG_WIDTH = 224
IMG_HEIGHT = IMG_WIDTH
DOT_SIZE = 16

SAMPLE_COUNT = 20
MAX_DOT_COUNT = 10

def create_dataset(folder, samples, is_test=False):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

    csv_data = []
    for sample in range(SAMPLE_COUNT):
        dot_ct = random.randint(1, MAX_DOT_COUNT)
        image = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), (255,255,255))
        draw = ImageDraw.Draw(image)

        for _ in range(dot_ct):
            x = random.randint(0, IMG_WIDTH - DOT_SIZE)
            y = random.randint(0, IMG_WIDTH - DOT_SIZE)
            draw.ellipse((x, y, x + DOT_SIZE, y + DOT_SIZE), fill="black") 

        del draw
        file_name = "%s/%s.png" % (folder, sample)
        image.save(file_name, "PNG")
        csv_data.append((sample, file_name, dot_ct))

    if is_test:
        df = pd.DataFrame(csv_data, columns=["id", "file", "count"])
        df.to_csv('%s/list.csv' % folder, index=False, columns=["id", "file"])
    else:
        df = pd.DataFrame(csv_data, columns=["id", "file", "count"])
        df.to_csv('%s/list.csv' % folder, index=False)


create_dataset("train", SAMPLE_COUNT, False)
create_dataset("test", SAMPLE_COUNT, True)
