#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class CrosslineApp(appier.App):
    """
    Top level class that is used as the entry point
    for the crossline application.
    """

    def __init__(self):
        appier.App.__init__(
            self,
            name = "crossline",
            service = True,
            parts = (
                appier_extras.AdminPart,
            )
        )

if __name__ == "__main__":
    app = CrosslineApp()
    app.serve()
