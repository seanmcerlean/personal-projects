import os
import sys
import unittest

from PIL import Image

sys.path.append(os.path.abspath('..'))
from ImageTools import *


class ImageSizeTest(unittest.TestCase):

    imfile = '/tmp/image.jpg'

    def setUp(self):
        im1 = Image.new('RGB', (256, 256), 'white')
        im1.save(self.imfile)

    def teardown(self):
        for file in [self.imfile, self.imfile.replace('.', '_cropped.'), self.imfile.replace('.', '_resized.')]:
            if os.path.isfile(file):
                os.remove(file)

    def test_get_image_width(self):
        img_width = ImageTools.get_image_width(self.imfile)
        self.assertEqual(img_width, '256')

    def test_get_image_width_error(self):
        img_width = ImageTools.get_image_width('.')
        self.assertEqual(img_width, 'Error opening file')

    def test_get_image_height(self):
        img_height = ImageTools.get_image_height(self.imfile)
        self.assertEqual(img_height, '256')

    def test_get_image_height_error(self):
        img_height = ImageTools.get_image_height('.')
        self.assertEqual(img_height, 'Error opening file')

    def test_get_image_size(self):
        img_size = ImageTools.get_image_size(self.imfile)
        self.assertEqual(img_size, (256, 256))

    def test_get_image_size_error(self):
        img_size = ImageTools.get_image_size('.')
        self.assertEqual(img_size, 'Error opening file')

    def test_crop_image(self):
        ImageTools.crop_image(self.imfile, 0, 0, 10, 10)
        cropped_size = ImageTools.get_image_size(self.imfile.replace('.', '_cropped.'))
        self.assertEqual(cropped_size, (10, 10))

    def test_crop_image_error(self):
        err = ImageTools.crop_image('.', 0, 0, 10, 10)
        self.assertEqual(err, 'Error opening file')

    def test_resize_image(self):
        ImageTools.resize_image(self.imfile, 500, 500)
        new_size = ImageTools.get_image_size(self.imfile.replace('.', '_resized.'))
        self.assertEqual(new_size, (500, 500))

    def test_resize_image_error(self):
        err = ImageTools.resize_image('.', 500, 500)
        self.assertEqual(err, 'Error opening file')


if __name__ == '__main__':
    unittest.main()
