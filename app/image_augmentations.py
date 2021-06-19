from PIL import Image, ImageFilter
import random
import numpy as np

def random_augmentation(image: Image):
    if max(image.size) > 1000:
        image = image.resize((700, 700))
    augmentations = [rotate, fliplr, do_nothing, blur]
    func = random.choice(augmentations)
    return func(image), func.__name__

def do_nothing(image: Image):
    return image

def fliplr(image: Image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def rotate(image: Image):
    return image.rotate(random.randint(1,359))

def blur(image: Image):
    #Let's handle possible failed image one after the other
    if image.mode == 'P':
        image = image.convert('RGB')
    return image.filter(ImageFilter.BLUR)