#!/usr/bin/python
# -*- coding: utf-8 -*-

import omni
import appier

from . import base

class OmniAdapter(base.BaseAdapter):

    def __init__(self):
        base.BaseAdapter.__init__(self)
        self._api = None

    @classmethod
    def ready(cls):
        enabled = appier.conf("OMNI_ENABLED", True, cast = bool)
        base_url = appier.conf("OMNI_BASE_URL")
        username = appier.conf("OMNI_USERNAME")
        password = appier.conf("OMNI_PASSWORD")
        return True if enabled and base_url and username and password else False

    def cross(self, info = None, app = None, *args, **kwargs):
        api = self.get_api()
        api.entries_sales_snapshot(dict(
            entry_chunk = dict(
                store_id = app,
                count = 1
            )
        ))

    def enter(self, info = None, app = None, *args, **kwargs):
        pass

    def get_api(self):
        if self._api: return self._api
        self._api = omni.API(
            base_url = appier.conf("OMNI_BASE_URL"),
            username = appier.conf("OMNI_USERNAME"),
            password = appier.conf("OMNI_PASSWORD")
        )
        return self._api
