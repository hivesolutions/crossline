#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from .. import base

class Action(base.CrosslineBase):

    timestamp = appier.field(
        type = int,
        index = "all",
        immutable = True
    )
