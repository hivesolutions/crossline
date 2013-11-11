#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import datetime

class ApiController(appier.Controller, appier.Mongo):

    @appier.controller("ApiController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)

    @appier.route("/api/cross", ("GET", "POST"))
    def cross(self):
        db = self.get_db("crossline")

        current = datetime.datetime.utcnow()

        filter = dict(
            year = current.year,
            month = current.month,
            day = current.day,
            hour = current.hour
        )

        fact = db.crossline.find_one(filter) or filter
        count = fact.get("count", 0) + 1
        fact["count"] = count

        db.crossline.save(fact)

        return count
