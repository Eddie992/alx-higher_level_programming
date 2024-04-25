#!/bin/bash
# This script takes in a url and displays the size in bytes
curl -s -o /dev/null -w "%{size_download}\n" $1
