#!/usr/bin/python3
"""This is a script that fetches a url using requests"""
import requests

if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body Response:")
    print("\t- type: {:}".format(type(fetch.text)))
    print("\t- content: {:}".format(fetch.text))
