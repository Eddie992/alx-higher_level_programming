#!/usr/bin/python3
"""This is a script that fetches a url"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        header = response.read()
        print("Body response:")
        print("\t- type: {:}".format(type(header)))
        print("\t- content: {:}".format(header))
        print("\t- utf8 content: {:}".format(header.decode('utf-8')))
