#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class CrosslineApp(appier.APIApp):
    """
    Top level class that is used as the entry point
    for the crossline application.
    """

    def __init__(self, *args, **kwargs):
        appier.APIApp.__init__(
            self,
            name = "crossline",
            service = True,
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )

if __name__ == "__main__":
    app = CrosslineApp()
    app.serve()
