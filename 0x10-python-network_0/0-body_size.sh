#!/bin/bash
# displays the size in bytes of a URL response header
curl -s "$1" | wc -c
