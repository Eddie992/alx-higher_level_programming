#!/usr/bin/python3
"""
A Module that contains  function that writes a string to a text file
"""


def write_file(filename=" ", text=" "):
    """
    function that writes text to file and returns number chars written

    Args:
        filename: the name of file to be written to
        text: the text to the written to the file

    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
