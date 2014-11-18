#!/usr/bin/python
# -*- coding: utf-8 -*-

import omni
import appier

from . import base

class OmniAdapter(base.BaseAdapter):

    def cross(self, app = None):
        api = self.get_api()
        api.snapshot_apply_entries(dict(
            store_id = app,
            count = 1
        ))

    def get_api(self):
        return omni.Api(
            base_url = appier.conf("OMNI_BASE_URL"),
            username = appier.conf("OMNI_USERNAME"),
            password = appier.conf("OMNI_PASSWORD")
        )
