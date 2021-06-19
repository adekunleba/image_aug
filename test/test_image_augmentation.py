import unittest

import numpy as np
from app.image_augmentations import do_nothing, fliplr, rotate, blur
from PIL import Image
import logging

class TestImageAugmentation(unittest.TestCase):

    def setUp(self) -> None:
        self.image_array = np.ones((224, 224, 3), dtype=np.uint8) * 128
        self.noise = np.random.randint(0, 127, self.image_array.shape, dtype=np.uint8)
        self.image_array = self.image_array + self.noise
        self.image =  Image.fromarray(self.image_array)


        self.small_image_array = np.ones((50, 50, 3), dtype=np.uint8) * 128
        self.small_noise = np.random.randint(0, 127, self.small_image_array.shape, dtype=np.uint8)
        self.small_image_array = self.small_image_array + self.small_noise
        self.small_image =  Image.fromarray(self.small_image_array)

    def test_do_nothing(self):
        aug_image = do_nothing(self.image)
        self.assertEqual(aug_image.size, self.image.size)

        self.assertEqual(np.array(aug_image).sum(), np.array(self.image).sum())

    def test_flip_right(self):
        
        flipped = fliplr(self.image)
        array_flipped = np.array(flipped)

        # Flip should turn pixels in left to right and vice versa
        self.assertEqual((array_flipped[:, 0, :] - self.image_array[:, -1, :]).sum(), 0)
        self.assertEqual((array_flipped[:, -1, :] - self.image_array[:, 0, :]).sum(), 0)

        # Image pixels sum should still be same
        self.assertEqual(array_flipped.sum(), self.image_array.sum())

    def test_rotate_image(self):

        rotated = rotate(self.image)
        array_rotated = np.array(rotated)

        # Sum of pixels should now be lower always cos rotation introduce pixel values 0
        self.assertLess(array_rotated[:, 0, :].sum(), self.image_array[:, 0, :].sum())

        # Once rotated, black padding is added to image, hence should not same
        self.assertNotEqual(array_rotated.sum(), self.image_array.sum())


    def test_add_noise(self):

        noised = blur(self.image)
        array_noised = np.array(noised)
        self.assertNotEqual(array_noised.sum(), self.image_array.sum())

        noised = blur(self.small_image)
        array_noised = np.array(noised)
        self.assertNotEqual(array_noised.sum(), self.small_image_array.sum())

if __name__ == '__main__':
    unittest.main()