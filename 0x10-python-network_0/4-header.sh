#!/bin/bash
# A scipt that sends a custom header to a server with a variable
curl -sH "X-School-User-Id: 98" "$1"
