"""Behavioural tests for pyflexebs' pure helpers.

normalize_device rewrites device names and is pure. configure_proxy
only mutates os.environ from ConfigProxy, so it is exercised by
setting the config and inspecting the environment afterwards.
"""

import os
import unittest

from pyflexebs import utils
from pyflexebs.configs import ConfigProxy
from pyflexebs.main import normalize_device


class NormalizeDeviceTests(unittest.TestCase):
    def test_rewrites_sd_to_xvd(self) -> None:
        self.assertEqual(normalize_device("/dev/sdb"), "/dev/xvdb")

    def test_rewrites_sd_multichar_suffix(self) -> None:
        self.assertEqual(normalize_device("/dev/sdaf"), "/dev/xvdaf")

    def test_leaves_non_sd_unchanged(self) -> None:
        self.assertEqual(normalize_device("/dev/xvdc"), "/dev/xvdc")
        self.assertEqual(normalize_device("/dev/nvme0n1"), "/dev/nvme0n1")


class ConfigureProxyTests(unittest.TestCase):
    _KEYS = (
        "http_proxy", "HTTP_PROXY",
        "https_proxy", "HTTPS_PROXY",
        "no_proxy", "NO_PROXY",
    )

    def setUp(self) -> None:
        self._saved_env = {k: os.environ.get(k) for k in self._KEYS}
        self._saved_cfg = (ConfigProxy.http_proxy, ConfigProxy.https_proxy, ConfigProxy.no_proxy)
        for k in self._KEYS:
            os.environ.pop(k, None)

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
        self.assertEqual(os.environ["http_proxy"], "http://proxy:3128")
        self.assertEqual(os.environ["HTTP_PROXY"], "http://proxy:3128")
        self.assertEqual(os.environ["https_proxy"], "http://proxy:3129")
        self.assertEqual(os.environ["HTTPS_PROXY"], "http://proxy:3129")
        self.assertEqual(os.environ["no_proxy"], "localhost")
        self.assertEqual(os.environ["NO_PROXY"], "localhost")

    def test_leaves_environment_untouched_when_none(self) -> None:
        ConfigProxy.http_proxy = None
        ConfigProxy.https_proxy = None
        ConfigProxy.no_proxy = None
        utils.configure_proxy()
        for k in self._KEYS:
            self.assertNotIn(k, os.environ)


if __name__ == "__main__":
    unittest.main()
