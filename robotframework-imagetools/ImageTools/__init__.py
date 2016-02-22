from ImageCompare import ImageCompare
from version import VERSION

_version_ = VERSION


class ImageTools(ImageCompare):
    ''' ImageTools is a Robot Framework keyword library to
    perform basic image manipulation and comparison
    '''
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'