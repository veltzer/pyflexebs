#!/bin/sh
docker build --tag pyflexebs:latest --file Dockerfile .
# everything is built, take a look
docker images
