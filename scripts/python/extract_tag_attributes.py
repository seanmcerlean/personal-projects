#!/usr/bin/python

"""
Simple script to extract attributes from a specified tag
e.g. href from a tags to see all links
"""
import argparse
import requests
from bs4 import BeautifulSoup, SoupStrainer

arguments = {
    'url': 'Webpage to extract from',
    'tag': 'Tag to search for',
    'attr': 'Attribute to extract'
}
parser = argparse.ArgumentParser()
for arg, description in arguments.iteritems():
   parser.add_argument(arg, help=description)

args = parser.parse_args()

response = requests.get(args.url)

for link in BeautifulSoup(response.text).find_all(args.tag):
    print(link.get(args.attr))
