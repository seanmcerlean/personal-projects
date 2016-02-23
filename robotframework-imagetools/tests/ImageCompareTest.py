import os
import sys
import unittest

from PIL import Image

sys.path.append(os.path.abspath('..'))
from ImageTools import *


class ImageCompareTest(unittest.TestCase):

    imfile1 = '/tmp/first.jpg'
    imfile2 = '/tmp/second.jpg'

    def setUp(self):
        for file in [self.imfile1, self.imfile2]:
            if os.path.isfile(file):
                os.remove(file)

    def test_equal_images_pixel_compare_returns_zero(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = im1.copy()

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_pixel(im1, im2)
        self.assertEqual(img_diff, 0 )

    def test_opposite_images_pixel_compare_returns_one_hundred(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = Image.new('RGB', (256, 256), 'black')

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_pixel(im1, im2)
        print(img_diff)
        self.assertEqual(img_diff, 100.0)

    def test_empty_images_pixel_compare_returns_error(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = None

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_pixel(im1, im2)
        self.assertEqual(img_diff, 'One or more images are empty' )

    def test_equal_images_histogram_compare_returns_zero(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = im1.copy()

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_histogram(im1, im2)
        self.assertEqual(img_diff, 0 )

    def test_opposite_images_histogram_compare_returns_nonzero(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = Image.new('RGB', (256, 256), 'black')

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_histogram(im1, im2)
        print(img_diff)
        self.assertGreater(img_diff, 0)

    def test_empty_images_histogram_compare_returns_error(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = None

        img_comp = ImageTools()
        img_diff = img_comp._compare_images_histogram(im1, im2)
        self.assertEqual(img_diff, 'One or more images are empty' )

    def test_imagefiles_calls_pixels_algo_by_default(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = Image.new('RGB', (256, 256), 'black')

        im1.save(self.imfile1)
        im2.save(self.imfile2)

        img_comp = ImageTools()
        img_diff = img_comp.compare_image_files(self.imfile1, self.imfile2)
        self.assertEqual(img_diff, 100.0)
    
    def test_imagefiles_calling_histogram_algo(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = Image.new('RGB', (256, 256), 'black')

        im1.save(self.imfile1)
        im2.save(self.imfile2)

        img_comp = ImageTools()
        img_diff = img_comp.compare_image_files(self.imfile1, self.imfile2, algorithm='histogram')
        self.assertGreater(img_diff, 100.0)
    
    def test_imagefiles_calling_unknown_algo_returns_error(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im2 = Image.new('RGB', (256, 256), 'black')

        im1.save(self.imfile1)
        im2.save(self.imfile2)

        img_comp = ImageTools()
        img_diff = img_comp.compare_image_files(self.imfile1, self.imfile2, algorithm='unknown')
        self.assertEqual(img_diff, 'Unsupported algorithm')

    def test_nonexist_imagefiles_return_error(self):
        im1 = Image.new('RGB', (256, 256), 'white')

        im1.save(self.imfile1)

        img_comp = ImageTools()
        img_diff = img_comp.compare_image_files(self.imfile1, 'notreal.jpg')
        self.assertEqual(img_diff, 'Error reading one or more files')

if __name__ == '__main__':
    unittest.main()
