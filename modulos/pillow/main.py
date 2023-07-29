from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

IMAGE_REF = ROOT_FOLDER / 'gato-animal-covid-19-scaled.jpg'

NEW_IMAGE = ROOT_FOLDER / 'new_image.jpg'

pil_image = Image.open(IMAGE_REF)

width, height = pil_image.size

try:
    exif = pil_image.info['exif']
    # Do something with the EXIF data, if needed.
except KeyError:
    # Handle the case where 'exif' key is not present in the 'info' dictionary.
    exif = None
    print("No EXIF data found for this image.")

new_width = 10000
new_height = round(height * new_width / width)  # Calculo
# print(width, height)
# print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(NEW_IMAGE,
               optimize=True,
               quality=70,
               )
