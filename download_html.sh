#!/bin/bash

wget -e robots=off -P data/  -U mozilla \
     --random-wait \
     --recursive \
     --no-clobber \
     --html-extension \
     --convert-links \
     --domains investopedia.com \
     --restrict-file-names=windows \
     --span-hosts \
     --no-parent \
         https://www.investopedia.com/financial-term-dictionary-4769738 
