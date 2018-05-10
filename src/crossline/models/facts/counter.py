#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

import appier

from . import fact

class CounterFact(fact.Fact):
    """
    Counter fact that handles the cross operation counting, meaning
    that whenever there's a new cross action the counter value
    should be incremented.
    """

    counter = appier.field(
        type = int,
        initial = 0,
        observations = """The integer counter value that should
        be incremented for every single interaction"""
    )

    action = appier.field(
        index = "hashed",
        immutable = True
    )

    @classmethod
    def increment_s(
        cls,
        app,
        adapters = [],
        current = None,
        action = "cross",
        *args,
        **kwargs
    ):
        current = current or datetime.datetime.utcnow()

        fact = cls.get(
            app = app,
            action = action,
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour,
            raise_e = False
        )
        if not fact: fact = cls(
            app = app,
            action = action,
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour
        )

        if not hasattr(fact, "counter"): fact.counter = 0
        fact.counter = fact.counter + 1
        fact.save()

        for adapter in adapters:
            method = getattr(adapter, action)
            method(app = app, **kwargs)

        return fact.counter
