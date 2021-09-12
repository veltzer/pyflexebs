import config.project

package_name = config.project.project_name

console_scripts = [
    'pyflexebs=pyflexebs.main:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',
    'pylogconf',
    'psutil',
    'boto3',
    'boto3-stubs',
    'pyfakeuse',
    'ec2-metadata',
    'pypathutil',
    'hurry.filesize',
    'bitmath',
    'python-daemon',
]

test_requires = [
    'pylint',
    'pytest',
    'pytest-cov',
    'pyflakes',
    'flake8',
    'pymakehelper',
]

dev_requires = [
    'pyclassifiers',
    'pypitools',
    'pydmt',
    'Sphinx',
    'pyinstaller',
    'pyapikey',
    'PyGithub',
    'gitpython',
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.7"

extras_require = {
}
test_os = "[ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.7, 3.8, 3.9]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
