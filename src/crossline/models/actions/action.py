#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

from .. import base

class Action(base.CrosslineBase):

    timestamp = appier.field(
        type = int,
        index = "all",
        immutable = True
    )

    @classmethod
    def list_names(cls):
        return ["created", "app"]

    @classmethod
    def order_name(cls):
        return ["id", -1]

    @classmethod
    def is_abstract(cls):
        return True

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        self.timestamp = int(time.time())
