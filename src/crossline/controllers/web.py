#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import datetime

class WebController(appier.Controller, appier.Mongo):

    @appier.controller("WebController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)

    @appier.route("/cross", "GET")
    @appier.route("/<app>/cross", "GET")
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
