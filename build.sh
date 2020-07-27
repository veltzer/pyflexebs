#!/bin/sh
rm -f docker/current.tar.gz
git archive -o docker/current.tar.gz HEAD
cd docker
docker build --tag pyflexebs:latest --file Dockerfile .
cd ..
id=$(docker create pyflexebs)
docker cp "$id:/home/user/pyflexebs/dist/pyflexebs-0.0.55" dist
docker rm -v $id
