#!/bin/bash
# a script that sends a POST request to a certain
# URL and displays the body response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"