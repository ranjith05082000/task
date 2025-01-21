from PIL import Image, ImageOps, ImageFilter
import numpy as np

def preprocess_image(image, target_size=(128, 32)):
    try:
        img = image.convert('L')
        img = ImageOps.autocontrast(img)
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        threshold = 128
        img = img.point(lambda p: p > threshold and 255)
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        img = np.array(img)
        img = np.expand_dims(img, axis=-1)
        img = img / 255.0
        return img
    except Exception as e:
        print(f"Error during image preprocessing: {e}")
        raise
