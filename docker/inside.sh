#!/bin/bash
cd pyflexebs
pip3 install --user .
pyinstaller pyflexebs.spec
