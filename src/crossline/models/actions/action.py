#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier

from .. import base

class Action(base.CrosslineBase):

    timestamp = appier.field(
        type = int,
        index = "all",
        safe = True,
        immutable = True,
        meta = "datetime",
        observations = """The snapshot timestamp for when
        the current action has occurred"""
    )

    info = appier.field(
        type = dict,
        immutable = True,
        observations = """Extra information associated with
        the action that can be used as a storage media"""
    )

    @classmethod
    def list_names(cls):
        return ["timestamp", "app"]

    @classmethod
    def order_name(cls):
        return ["id", -1]

    @classmethod
    def is_abstract(cls):
        return True

    @classmethod
    def get_by_entity(cls, entity, *args, **kwargs):
        return cls.get_e(entity = entity, *args, **kwargs)

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        if not hasattr(self, "timestamp") or not self.timestamp:
            self.timestamp = int(time.time())
