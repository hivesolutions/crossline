#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Fact(base.CrosslineBase):

    year = appier.field(
        type = int,
        index = "hashed"
    )

    month = appier.field(
        type = int,
        index = "hashed"
    )

    day = appier.field(
        type = int,
        index = "hashed"
    )

    hour = appier.field(
        type = int,
        index = "hashed"
    )
