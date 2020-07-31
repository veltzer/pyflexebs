import config.project

package_name = config.project.project_name

console_scripts = [
    'pyflexebs=pyflexebs.endpoints.main:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',  # for command line parsing
    'pylogconf',  # for logging configuration
    'psutil',  # for partition information
    'boto3',  # for aws API
    'boto3-stubs',  # for aws API
    'pyfakeuse',  # for fake use
    'ec2-metadata',  # for metadata
    'pypathutil',  # for checking path elements
    'hurry.filesize',  # for printing sizes
    'bitmath',  # to do calculations of bytes
    'python-daemon',  # for daemonization
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pyflakes',  # for testing
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
    'pyinstaller',  # for creating a single executable
    'pyapikey',  # for getting github key
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
