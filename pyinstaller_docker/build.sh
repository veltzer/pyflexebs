#!/bin/sh
rm -f /tmp/current.tar.gz
git archive -o /tmp/current.tar.gz HEAD
docker build --tag pyflexebs:latest --file pyinstaller_docker/Dockerfile .
id=$(docker create pyflexebs)
docker cp "$id:/home/user/pyflexebs/dist/pyflexebs-0.0.55" dist
docker rm -v $id
