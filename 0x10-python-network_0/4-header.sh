#!/bin/bash
# takes in an URL as an arguement, sends a GET requeat to the URL
curl -sH "X-School-User-Id: 98" "$1"
