from typing import List


console_scripts: List[str] = [
    "pyflexebs=pyflexebs.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
    "pyinstaller",
    "pyapikey",
    "PyGithub",
    "gitpython",
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
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
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
requires = config_requires + install_requires + make_requires + test_requires
