import configparser
from selenium import webdriver

drivers = {
    'Firefox': webdriver.Firefox,
    'Chrome': webdriver.Chrome
}

def before_all(context):
    config = configparser.ConfigParser()
    config.read('config.ini')
    context.config = config
    context.browser = config['DEFAULT']['Browser']
    context.base_url = config['DEFAULT']['BaseURL']

def before_feature(context, feature):
    driver = drivers[context.browser]()
    context.driver = driver

def after_feature(context, feature):
    driver = context.driver
    driver.close()