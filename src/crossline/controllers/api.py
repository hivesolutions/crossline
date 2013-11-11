#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class ApiController(appier.Controller):

    @appier.controller("BaseController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)

    @appier.route("/cross", ("GET", "POST"))
    def index(self):
        return self.template(
            "index.html.tpl"
        )

    @appier.route("/hello/<int:name>", "GET")
    def hello(self, name):
        return dict(
            name = name
        )
