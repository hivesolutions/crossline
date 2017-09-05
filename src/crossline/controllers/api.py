#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import appier

import crossline

ROW_ORDER = (
    "app",
    "year",
    "month",
    "day",
    "hour",
    "counter"
)
""" The list defining the sequence of the various
columns to be used in the creation of the rows """

class APIController(appier.Controller, appier.Mongo):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)
        self.adapters = crossline.get_adapters()

    @appier.route("/api/cross", ("GET", "POST"))
    @appier.route("/api/<str:app>/cross", ("GET", "POST"))
    def cross(self, app = None):
        return crossline.CounterFact.increment_s(app, self.adapters)

    @appier.route("/api/facts", "GET")
    @appier.route("/api/<str:app>/facts", "GET")
    def facts(self, app = None):
        object = appier.get_object(
            alias = True,
            find = True,
            sort = [("_id", -1)]
        )
        if app: object["app"] = app
        facts = crossline.CounterFact.find(map = True, **object)
        return facts

    @appier.route("/api/facts.csv", "GET")
    @appier.route("/api/<str:app>/facts.csv", "GET")
    def facts_csv(self, app = None):
        object = appier.get_object(
            alias = True,
            find = True,
            sort = [("_id", -1)]
        )
        if app: object["app"] = app
        facts = crossline.CounterFact.find(map = True, **object)

        buffer = appier.legacy.StringIO()
        writer = csv.writer(buffer, delimiter = ";")
        writer.writerow(ROW_ORDER)

        for fact in facts:
            row = []
            for name in ROW_ORDER:
                value = fact[name]
                row.append(value)
            writer.writerow(row)

        data = buffer.getvalue()

        self.content_type("text/csv")
        return data
