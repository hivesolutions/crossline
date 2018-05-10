#!/usr/bin/python
# -*- coding: utf-8 -*-

import crossline

from . import base

class LocalAdapter(base.BaseAdapter):

    def __init__(self):
        base.BaseAdapter.__init__(self)
        self._api = None

    @classmethod
    def ready(cls):
        return True

    def cross(self, app = None, *args, **kwargs):
        pass

    def entry(self, app = None, *args, **kwargs):
        payload = kwargs.get("payload", {})
        entity = payload.get("entity", None)
        if not entity: return
        crossline.EntryAction.entry_s(entity)
