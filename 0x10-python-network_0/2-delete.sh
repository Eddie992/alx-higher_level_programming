#!/bin/bash
# A script that sends a delete message to a website and returns the body
curl -sX DELETE "$1"
