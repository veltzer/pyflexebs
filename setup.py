import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pyflexebs",
    version="0.0.89",
    packages=[
        "pyflexebs",
    ],
    # from here all is optional
    description="Pyflexebs will allow you to monitor and expand/contract you EBS volumes in aws",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "aws",
        "ebs",
    ],
    url="https://veltzer.github.io/pyflexebs",
    download_url="https://github.com/veltzer/pyflexebs",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
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
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": [
        "pyflexebs=pyflexebs.main:main",
    ]},
)
