#!/usr/bin/env python

import subprocess
import config.version

# subprocess.check_call([
#    "hub",
#    "release",
#    "create",
#    "-a",
#    "dist/pyflexebs-{}".format(config.version.version_str),
#    "-m",
#    "version {}".format(config.version.version_str),
#    config.version.version_str,
# ])

subprocess.check_call([
    "git",
    "tag",
    config.version.version_str,
])
subprocess.check_call([
    "git",
    "push",
    "--tags",
])
subprocess.check_call([
    "github-release",
    "release",
    "--user",
    "veltzer",
    "--repo",
    "pyflexebs",
    "--tag",
    config.version.version_str,
    "--name",
    "version {}".format(config.version.version_str),
])
subprocess.check_call([
    "github-release",
    "upload",
    "--user",
    "veltzer",
    "--repo",
    "pyflexebs",
    "--tag",
    config.version.version_str,
    "--name",
    "pyflexebs-{}".format(config.version.version_str),
    "--file",
    "dist/pyflexebs-{}".format(config.version.version_str),
])
