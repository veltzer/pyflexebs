#!/usr/bin/env python

import subprocess
import config.version

subprocess.check_call([
    "hub",
    "release",
    "create",
    "-a",
    "dist/pyflexebs-{}".format(config.version.version_str),
    "-m",
    "version {}".format(config.version.version_str),
    config.version.version_str,
])
