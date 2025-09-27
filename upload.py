from PIL import Image
import numpy as np

def upload_image(file_path):
    image = Image.open(file_path)
    image = image.convert("RGB")  # Ensure it's in Red, Gren, Blue
    return np.array(image)  # Convert to Numpy

