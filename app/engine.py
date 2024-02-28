import os
from PIL import Image


def get_tiff_file(path):
    for file in os.listdir(path):
        if file.endswith(".png"):
            image = Image.open(f'app/image_files/{file}', 'r')
            image.save("app/Result.tif", 'TIFF')
    print('Файлы успешно собраны!')
