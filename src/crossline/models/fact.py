#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base

class Fact(base.CrosslineBase):

    year = appier.field(
        type = int,
        index = True
    )

    month = appier.field(
        type = int,
        index = True
    )

    day = appier.field(
        type = int,
        index = True
    )

    hour = appier.field(
        type = int,
        index = True
    )
