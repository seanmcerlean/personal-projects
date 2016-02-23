from ImageCompare import ImageCompare
from ImageSize import ImageSize
from version import VERSION

_version_ = VERSION


class ImageTools(ImageCompare, ImageSize):
    ''' ImageTools is a Robot Framework keyword library to
    perform basic image manipulation and comparison
    '''
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'