"""Behavioural tests for pyflexebs' pure helpers.

normalize_device rewrites device names and is pure. configure_proxy
only mutates os.environ from ConfigProxy, so it is exercised by
setting the config and inspecting the environment afterwards.
"""

import os
import unittest
from typing import override

from pyflexebs import utils
from pyflexebs.configs import ConfigProxy
from pyflexebs.main import normalize_device


class NormalizeDeviceTests(unittest.TestCase):
    def test_rewrites_sd_to_xvd(self) -> None:
        assert normalize_device("/dev/sdb") == "/dev/xvdb"

    def test_rewrites_sd_multichar_suffix(self) -> None:
        assert normalize_device("/dev/sdaf") == "/dev/xvdaf"

    def test_leaves_non_sd_unchanged(self) -> None:
        assert normalize_device("/dev/xvdc") == "/dev/xvdc"
        assert normalize_device("/dev/nvme0n1") == "/dev/nvme0n1"


class ConfigureProxyTests(unittest.TestCase):
    _KEYS = (
        "http_proxy", "HTTP_PROXY",
        "https_proxy", "HTTPS_PROXY",
        "no_proxy", "NO_PROXY",
    )

    @override
    def setUp(self) -> None:
        self._saved_env = {k: os.environ.get(k) for k in self._KEYS}
        self._saved_cfg = (ConfigProxy.http_proxy, ConfigProxy.https_proxy, ConfigProxy.no_proxy)
        for k in self._KEYS:
            os.environ.pop(k, None)

    @override
    def tearDown(self) -> None:
        for k, v in self._saved_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        ConfigProxy.http_proxy, ConfigProxy.https_proxy, ConfigProxy.no_proxy = self._saved_cfg

    def test_sets_both_case_variants_when_configured(self) -> None:
        ConfigProxy.http_proxy = "http://proxy:3128"
        ConfigProxy.https_proxy = "http://proxy:3129"
        ConfigProxy.no_proxy = "localhost"
        utils.configure_proxy()
        assert os.environ["http_proxy"] == "http://proxy:3128"
        assert os.environ["HTTP_PROXY"] == "http://proxy:3128"
        assert os.environ["https_proxy"] == "http://proxy:3129"
        assert os.environ["HTTPS_PROXY"] == "http://proxy:3129"
        assert os.environ["no_proxy"] == "localhost"
        assert os.environ["NO_PROXY"] == "localhost"

    def test_leaves_environment_untouched_when_none(self) -> None:
        ConfigProxy.http_proxy = None
        ConfigProxy.https_proxy = None
        ConfigProxy.no_proxy = None
        utils.configure_proxy()
        for k in self._KEYS:
            assert k not in os.environ


if __name__ == "__main__":
    unittest.main()
