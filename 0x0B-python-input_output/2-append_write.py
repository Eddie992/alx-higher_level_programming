#!/usr/bin/python3
"""A module that appends a string at the end of a file"""


def append_write(filename=" ", text=" "):
    """
    This function appends a string at the end of a file
    Args:
        filename: is the name of the file to append
        text: is the string to be appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
