from collections import namedtuple

Locator = namedtuple('Locator', ['Type', 'Value'])

class BasePage():
    def __init__(self, driver):
        self.driver = driver
