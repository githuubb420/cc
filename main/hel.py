import yaml
import os
from envparse import env
from typing import Any
from main.helper.logger import log

DEFAULTS = {}


def get_int(name, req=True):
    default = DEFAULTS[name] if name in DEFAULTS else None
    data = env.int(name, default=default)
    if data and req:
        return data
    elif not data and req:
        return None
    elif not data and not req:
        log.warn("No Var found: {}".format(name))
        exit()
    else:
        return data


def get_str(name, req=True):
    default = DEFAULTS[name] if name in DEFAULTS else None
    data = env.str(name, default=default)
    if data and req:
        return data
    elif not data and req:
        return None
    elif not data and not req:
        log.warn("No Var found: {}".format(name))
        exit()
    else:
        return data


def get_bool(name, req=True):
    default = DEFAULTS[name] if name in DEFAULTS else None
    data = env.bool(name, default=default)
    if data and req:
        return data
    elif not data and req:
        return None
    elif not data and not req:
        log.warn("No Var found: {}".format(name))
        exit()
    else:
        return data


def get_list(name, req=True):
    default = DEFAULTS[name] if name in DEFAULTS else None
    data = env.list(name, default=default)
    if data and req:
        return data
    elif not data and req:
        return None
    elif not data and not req:
        log.warn("No Var found: {}".format(name))
        exit()
    else:
        return data
