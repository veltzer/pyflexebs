""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "psutil",
    "boto3",
    "boto3-stubs",
    "pyfakeuse",
    "ec2-metadata",
    "pypathutil",
    "hurry.filesize",
    "bitmath",
    "python-daemon",
    "pyinstaller",
    "pyapikey",
    "PyGithub",
    "gitpython",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
types_requires: list[str] = [
    "types-psutil",
]
requires = install_requires + build_requires + test_requires + types_requires

scripts: dict[str,str] = {
    "pyflexebs": "pyflexebs.main:main",
}
