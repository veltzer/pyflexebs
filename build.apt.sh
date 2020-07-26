#!/bin/sh
sudo apt install python3-pip python3-dev gcc
pip3 install --user . pyinstaller
pyinstaller pyflexebs.spec
