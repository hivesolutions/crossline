#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class PicaAdapter(base.BaseAdapter):
    """
    Simple adapter for the PicaPinto website to be used
    for the enter actions to be created.

    :see: https://picaponto.pt
    """

    def __init__(self):
        base.BaseAdapter.__init__(self)
        self._api = None

    @classmethod
    def ready(cls):
        base_url = appier.conf("PICA_BASE_URL", "https://picaponto.pt/")
        company = appier.conf("PICA_COMPANY", cast = int)
        return True if base_url and company else False

    def cross(self, info = None, app = None, *args, **kwargs):
        pass

    def enter(self, info = None, app = None, *args, **kwargs):
        base_url = appier.conf("PICA_BASE_URL", "https://picaponto.pt/")
        company = appier.conf("PICA_COMPANY", None, cast = int)
        appier.post(
            base_url + "ponto/ajax_add",
            empresa_id = company,
            codigo = 123, #@todo be used the one from metadata
            senha = 123123, #@todo be used the one from metadata
            tipo_movimento = "Entrada" #todo should be inferred according to some rules
        )
