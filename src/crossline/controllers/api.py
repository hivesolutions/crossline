#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import datetime

class ApiController(appier.Controller, appier.Mongo):

    @appier.controller("ApiController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)

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
        db = self.get_db("crossline")

        filter = dict(
            app = app
        )

        cursor = db.facts.find(filter)
        facts = [fact for fact in cursor]
        for fact in facts: del fact["_id"]

        return dict(
            facts = facts
        )
