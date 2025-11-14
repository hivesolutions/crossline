#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras


class CrosslineBase(appier_extras.admin.Base):

    app = appier.field(index="hashed")

    @classmethod
    def is_abstract(cls):
        return True

    @appier.operation(name="Set App", parameters=(("App", "app", str),))
    def set_app_s(self, app=None):
        app = app or None
        self.app = app
        self.save()
