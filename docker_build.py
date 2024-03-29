#!/usr/bin/env python

import subprocess
import tempfile
import shutil
import os
import config.version
from pydmt.helpers.misc import get_version_str

version_str = get_version_str()
dir_path = tempfile.mkdtemp()
orig_path = os.getcwd()
tar_file = os.path.join(dir_path, "current.tar.gz")
if os.path.isfile(tar_file):
    os.unlink(tar_file)
subprocess.check_call([
    "git",
    "archive",
    "-o",
    tar_file,
    "HEAD",
])
shutil.copy("Dockerfile", dir_path)
os.chdir(dir_path)
subprocess.check_call([
    "docker",
    "build",
    "--tag",
    "pyflexebs:latest",
    "--file",
    "Dockerfile",
    ".",
])
os.chdir(orig_path)
shutil.rmtree(dir_path)
container_id = subprocess.check_output([
    "docker",
    "create",
    "pyflexebs",
]).decode().rstrip()
subprocess.check_call([
    "docker",
    "cp",
    f"{container_id}:/home/user/pyflexebs/dist/pyflexebs",
    f"dist/pyflexebs-{version_str}"
])
subprocess.check_call([
    "docker",
    "rm",
    container_id,
])
