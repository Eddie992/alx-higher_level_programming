#!/bin/bash
# This script send a POST request with specific parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
