#!/usr/bin/python3
"""This is a script that takes a url and displays the value of X-Request-Id"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
