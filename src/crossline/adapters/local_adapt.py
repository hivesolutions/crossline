#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import base

class LocalAdapter(base.BaseAdapter):

    def __init__(self):
        base.BaseAdapter.__init__(self)
        self._api = None

    @classmethod
    def ready(cls):
        pass

    def cross(self, app = None, *args, **kwargs):
        pass

    def entry(self, app = None, *args, **kwargs):
        pass
