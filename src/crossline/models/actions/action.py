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

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        self.timestamp = int(time.time())
