#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class CrosslineBase(appier_extras.admin.Base):

    app = appier.field(
        index = "hashed"
    )
