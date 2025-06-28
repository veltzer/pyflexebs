#!/bin/sh
sudo yum install python3-pip python3-devel gcc
pip3 install --user . pyinstaller
pyinstaller pyflexebs.spec
