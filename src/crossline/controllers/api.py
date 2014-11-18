#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import appier
import datetime

import crossline.adapters

ROW_ORDER = (
    "app",
    "year",
    "month",
    "day",
    "hour",
    "count"
)
""" The list defining the sequence of the various
columns to be used in the creation of the rows """

ADAPTERS = (
    crossline.adapters.BaseAdapter,
    crossline.adapters.OmniAdapter
)
""" The sequence defining the complete set of adapter
classes that may be used for runtime notification """

class ApiController(appier.Controller, appier.Mongo):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)
        self.adapters = self._get_adapters()

    @appier.route("/api/cross", "GET")
    @appier.route("/api/<app>/cross", "GET")
    def cross(self, app = None):
        db = self.get_db("crossline")

        current = datetime.datetime.utcnow()

        filter = dict(
            app = app,
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour
        )

        fact = db.facts.find_one(filter) or filter
        count = fact.get("count", 0) + 1
        fact["count"] = count

        db.facts.save(fact)

        return count

    @appier.route("/api/facts", "GET")
    @appier.route("/api/<app>/facts", "GET")
    def facts(self, app = None):
        count = self.field("count", 30, cast = int)
        db = self.get_db("crossline")

        filter = dict()
        if app: filter["app"] = app

        cursor = db.facts.find(
            filter,
            sort = [("_id", -1)],
            limit = count
        )
        facts = [fact for fact in cursor]
        for fact in facts: del fact["_id"]

        return dict(
            facts = facts
        )

    @appier.route("/api/facts.csv", "GET")
    @appier.route("/api/<app>/facts.csv", "GET")
    def facts_csv(self, app = None):
        count = self.field("count", 30, cast = int)
        db = self.get_db("crossline")

        filter = dict()
        if app: filter["app"] = app

        cursor = db.facts.find(
            filter,
            sort = [("_id", -1)],
            limit = count
        )

        buffer = appier.legacy.StringIO()
        writer = csv.writer(buffer, delimiter = ";")
        writer.writerow(ROW_ORDER)

        facts = [fact for fact in cursor]
        for fact in facts:
            row = []
            for name in ROW_ORDER:
                value = fact[name]
                row.append(value)
            writer.writerow(row)

        data = buffer.getvalue()

        self.content_type("text/csv")
        return data

    def _get_adapters(self):
        adapters = []
        for adapter_c in ADAPTERS:
            if not adapter_c.ready(): continue
            adapter = adapter_c()
            adapters.append(adapter)
        return adapters
