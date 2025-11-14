#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier


class Day(appier.Model):

    year = appier.field(type=int, index="hashed")

    month = appier.field(type=int, index="hashed")

    day = appier.field(type=int, index="hashed", immutable=True)

    hour = appier.field(type=int, index="hashed", immutable=True)

    timestamp = appier.field(type=int, index="all", immutable=True)

    @classmethod
    def is_abstract(cls):
        return True
