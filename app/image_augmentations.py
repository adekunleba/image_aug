from PIL import Image, ImageFilter
import random
import numpy as np


def random_augmentation(image: Image):
    augmentations = [rotate, fliplr, do_nothing, blur]
    func = random.choice(augmentations)
    return func(image)

def do_nothing(image: Image):
    return image

def fliplr(image: Image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def rotate(image: Image):
    return image.rotate(random.randint(0,365))

def blur(image: Image):
    return image.filter(ImageFilter.BLUR)