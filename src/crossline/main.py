#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class CrosslineApp(appier.App):
    """
    Top level class that is used as the entry point
    for the crossline application.
    """

    def __init__(self):
        appier.App.__init__(
            self,
            name = "crossline",
            service = True
        )
        self.count = 0

    @appier.route("/", "GET")
    @appier.route("/counter", "GET")
    def counter(self):
        return dict(
            count = self.count
        )

    @appier.route("/cross", ("GET", "POST"))
    def cross(self, data = None):
        self.count += 1
        return "OK"

if __name__ == "__main__":
    app = CrosslineApp()
    app.serve(env = True)
