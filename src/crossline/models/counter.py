#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

import appier

from . import fact

class CounterFact(fact.Fact):

    counter = appier.field(
        type = int,
        index = True
    )

    @classmethod
    def increment_s(cls, app, adapters, *args, **kwargs):
        current = datetime.datetime.utcnow()

        fact = cls.get(
            app = app,
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour,
            raise_e = False
        )
        if not fact: fact = cls(
            app = app,
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour
        )

        if not hasattr(fact, "counter"): fact.counter = 0
        fact.counter = fact.counter + 1
        fact.save()

        for adapter in adapters: adapter.cross(app = app)

        return fact.counter
