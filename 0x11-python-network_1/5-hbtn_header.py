#!/usr/bin/python3
"""This is a script that displays the value of X-Request-Id"""
import requests
from sys import argv

if __name__ == "__main__":
    fetch = requests.get(argv[1])
    print(fetch.headers.get('X-Request-Id'))
