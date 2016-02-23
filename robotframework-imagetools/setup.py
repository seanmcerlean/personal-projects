import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "robotframework_imagetools",
    version = "0.0.1",
    author = "Sean mcerlean",
    author_email = "seanmcerlean82@gmail.com",
    description = ("A wrapper around python image for robotframework to perform some basic image manipulations."),
    license = "Apache",
    keywords = "robotframework pil image comparison",
    url = "https://github.com/seanmcerlean/personal-projects.git",
    packages=['ImageTools', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Automation",
        "License :: GNU GENERAL PUBLIC LICENSE",
    ],
    install_requires=[
          'pillow',
          'robotframework',
    ],
)
