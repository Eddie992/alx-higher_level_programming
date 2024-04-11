#!/usr/bin/python3
"""
This script takes a url and an email and sends a POST request
"""
import sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    send = urllib.request.Request(url, data)
    with urllib.request.urlopen(send) as response:
        result = response.read()
        print(result.decode('utf-8'))
