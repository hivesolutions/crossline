#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class WebController(appier.Controller, appier.Mongo):

    @appier.controller("WebController")
    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        appier.Mongo.__init__(self, *args, **kwargs)
