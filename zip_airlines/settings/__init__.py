from configurations import Configuration

from .base import BaseSettings
from .database import DataBaseSettings


class CommonConfiguration(
    BaseSettings,
    DataBaseSettings,
    Configuration,
):
    pass


class Dev(CommonConfiguration):
    DEBUG = True


class Prod(CommonConfiguration):
    pass
