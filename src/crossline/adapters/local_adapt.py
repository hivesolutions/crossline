#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import crossline

from . import base

class LocalAdapter(base.BaseAdapter):

    def __init__(self):
        base.BaseAdapter.__init__(self)
        self._api = None

    @classmethod
    def ready(cls):
        enabled = appier.conf("OMNI_ENABLED", True, cast = bool)
        return enabled

    def cross(self, info = None, app = None, *args, **kwargs):
        pass

    def enter(self, info = None, app = None, *args, **kwargs):
        info = info or dict()
        payload = kwargs.get("payload", {})
        entity = payload.get("entity", None)
        key = payload.get("key", None)
        if not entity or not key: return
        if not info.get("save", True): return
        enter = crossline.EnterAction.enter_s(
            entity,
            info = info,
            key = key,
            verify = True
        )
        info.update(
            enter = dict(
                timestamp = enter.timestamp,
                entity = enter.entity.identifier
            )
        )
