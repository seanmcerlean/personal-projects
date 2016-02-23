from PIL import Image

class ImageSize():
    """
    Providses size information and crop / resize tools for images
    """
    def __init__(self):
        pass

    def _open_image_file(function):
        """
        Decorator to open image file
        """
        def read_image(image_file, *args):
            try:
                image = Image.open(image_file)
                return function(image, *args)
            except IOError:
                return 'Error opening file'

        return read_image

    @staticmethod
    @_open_image_file
    def get_image_size(image):
        """

        :param image_file: A path to an image file
        :return: The size of the image as (width, height) tuple
        """
        return image.size

    @staticmethod
    @_open_image_file
    def get_image_width(image):
        """

        :param image_file: A path to an image file
        :return: The width of the image as a string
        """
        return str(image.size[0])

    @staticmethod
    @_open_image_file
    def get_image_height(image):
        """

        :param image_file: A path to an image file
        :return: The height of an image as a string
        """
        return str(image.size[1])

    @staticmethod
    def crop_image(image_file, left, upper, right, lower):
        """
        Opens an image, crops it and saves to the same location as image_cropped.ext
        The top left of the image is point (0, 0)
        :param image_file: Location of the image
        :param left:  leftmost point of crop area
        :param upper: uppermost point of crop area
        :param right: rightmost point of crop area
        :param lower: lowest point of crop area
        :return: None
        """
        try:
            image = Image.open(image_file)
            crop_area = (int(left), int(upper), int(right), int(lower))
            cropped_image = image.crop(box=crop_area)
            cropped_image.save(image_file.replace('.', '_cropped.'))
        except IOError:
            return 'Error opening file'

    @staticmethod
    def resize_image(image_file, width, height):
        """
        Opens an image, resizes it and saves to the same location as image_resized.ext
        If enlarging the image, uses a nearest neignbour resample
        :param image_file: Location of the image
        :param width: width of new image
        :param height: height of new image
        :return: None
        """
        try:
            image = Image.open(image_file)
            new_size = (int(width), int(height))
            new_image = image.resize(size=new_size)
            new_image.save(image_file.replace('.', '_resized.'))
        except IOError:
            return 'Error opening file'