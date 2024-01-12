from typing import List


console_scripts: List[str] = [
    "pyflexebs=pyflexebs.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "pyinstaller",
    "pyapikey",
    "PyGithub",
    "gitpython",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires = [
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
]
build_requires = [
    "pymakehelper",
    "pydmt",
    "types-psutil",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
