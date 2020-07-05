"""
All configurations for pyflexebs
"""


from pytconf.config import Config, ParamCreator


class ConfigInterval(Config):
    """
    Parameters for interval monitoris
    """
    filenames = ParamCreator.create_int(
    )
