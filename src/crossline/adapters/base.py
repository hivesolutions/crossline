#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class BaseAdapter(object):

    @classmethod
    def ready(cls):
        return True

    def cross(self, app = None, *args, **kwargs):
        raise appier.NotImplementedError()

    def entry(self, app = None, *args, **kwargs):
        raise appier.NotImplementedError()
