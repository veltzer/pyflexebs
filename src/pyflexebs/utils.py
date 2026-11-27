""" utils.py """

import logging
import os
import sys
from logging import Logger
from subprocess import PIPE, Popen

import pypathutil.common

import pyflexebs
from pyflexebs.configs import ConfigProxy


def run_with_logger(args: list[str], logger: logging.Logger) -> None:
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    all_args = ",".join(args)
    logger.info("running [%s]", all_args)
    with Popen(args, stdout=PIPE, stderr=PIPE) as proc:
        out, err = proc.communicate()
        exitcode = proc.returncode
    if exitcode != 0:
        logger.error("error in execution with code [%s]", exitcode)
        logger.debug("stdout was [%s]", out.decode())
        logger.debug("stderr was [%s]", err.decode())
    else:
        logger.info("execution was successful")


def get_logger() -> Logger:
    return logging.getLogger(pyflexebs.LOGGER_NAME)


def check_root() -> None:
    if os.geteuid() != 0:
        sys.exit("Script must be run as root")


def configure_proxy() -> None:
    if ConfigProxy.http_proxy is not None:
        os.environ["http_proxy"] = ConfigProxy.http_proxy
        os.environ["HTTP_PROXY"] = ConfigProxy.http_proxy
    if ConfigProxy.https_proxy is not None:
        os.environ["https_proxy"] = ConfigProxy.https_proxy
        os.environ["HTTPS_PROXY"] = ConfigProxy.https_proxy
    if ConfigProxy.no_proxy is not None:
        os.environ["no_proxy"] = ConfigProxy.no_proxy
        os.environ["NO_PROXY"] = ConfigProxy.no_proxy


def check_tools() -> None:
    """
    Check that the command line tools we need are available
    """
    logger = get_logger()
    problems = False
    for app in ["xfs_growfs", "resize2fs"]:
        if pypathutil.common.find_in_standard_path(app) is None:
            problems = True
            logger.error("please install executable [%s]", app)
    if problems:
        sys.exit(1)


def dump(obj: object) -> None:
    """
    debugging function to dump objects
    """
    for attr in dir(obj):
        if attr.startswith("__"):
            continue
        print(f"obj.{attr} = {getattr(obj, attr)}")
