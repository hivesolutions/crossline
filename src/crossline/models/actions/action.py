#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

from .. import base

class Action(base.CrosslineBase):

    timestamp = appier.field(
        type = int,
        index = "all",
        safe = True,
        immutable = True,
        meta = "datetime",
        observations = """The snapshot timestamp for when
        the current action has occurred"""
    )

    @classmethod
    def list_names(cls):
        return ["timestamp", "app"]

    @classmethod
    def order_name(cls):
        return ["id", -1]

    @classmethod
    def is_abstract(cls):
        return True

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        self.timestamp = int(time.time())
