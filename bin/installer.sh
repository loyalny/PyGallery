#!/bin/sh

pip3 install -r ../requirements.txt

pyinstaller --noconsole --onefile --name="PyGallery"  ../src/python/main.py

read
