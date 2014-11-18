#!/usr/bin/python
# -*- coding: utf-8 -*-

class BaseAdapter(object):

    @classmethod
    def ready(cls):
        return True

    def cross(self, app = None):
        pass
