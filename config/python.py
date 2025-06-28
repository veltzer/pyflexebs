""" python deps for this project """

scripts: dict[str,str] = {
    "pyflexebs": "pyflexebs.main:main",
}
config_requires: list[str] = [
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
    "pydmt",
    "pymakehelper",

    "pyinstaller",
    "pyapikey",
    "PyGithub",
    "gitpython",
]
test_requires = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
    # types
    "types-psutil",
]
requires = config_requires + install_requires + build_requires + test_requires
