#!/usr/bin/env python

import subprocess
import os
import config.version

tarfile = "docker/current.tar.gz"
if os.path.isfile(tarfile):
    os.unlink(tarfile)
subprocess.check_call([
    "git",
    "archive",
    "-o",
    tarfile,
    "HEAD",
])
os.chdir("docker")
subprocess.check_call([
    "docker",
    "build",
    "--tag",
    "pyflexebs:latest",
    "--file",
    "Dockerfile",
    ".",
])
os.chdir("..")
container_id = subprocess.check_output([
    "docker",
    "create",
    "pyflexebs",
]).decode().rstrip()
subprocess.check_call([
    "docker",
    "cp",
    "{}:/home/user/pyflexebs/dist/pyflexebs".format(
        container_id,
    ),
    "dist/pyflexebs-{}".format(
        config.version.version_str,
    ),
])
subprocess.check_call([
    "docker",
    "rm",
    container_id,
])
