#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import crossline

class WebController(appier.Controller, appier.Mongo):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)
        self.adapters = crossline.get_adapters()

    @appier.route("/cross", ("GET", "POST"))
    @appier.route("/<str:app>/cross", ("GET", "POST"))
    def cross(self, app = None):
        return crossline.CounterFact.increment_s(
            app,
            adapters = self.adapters,
            action = "cross"
        )

    @appier.route("/enter", ("GET", "POST"))
    @appier.route("/<str:app>/enter", ("GET", "POST"))
    def entry(self, app = None):
        return crossline.CounterFact.increment_s(
            app,
            adapters = self.adapters,
            action = "entry",
            payload = self.request.get_data()
        )
