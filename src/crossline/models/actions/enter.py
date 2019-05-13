#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import action
from .. import entity

class EnterAction(action.Action):

    entity = appier.field(
        type = appier.reference(
            entity.Entity,
            name = "identifier"
        ),
        observations = """The entity that has just entered
        a certain area of coverage"""
    )

    @classmethod
    def list_names(cls):
        return ["timestamp", "entity", "app"]

    @classmethod
    def latest(cls, identifier):
        return cls.get(
            entity = identifier,
            sort = [("timestamp", -1), ("id", -1)],
            raise_e = False
        )

    @classmethod
    def last(cls, identifier, limit = 2):
        return cls.find(
            entity = identifier,
            sort = [("timestamp", -1), ("id", -1)],
            limit = limit
        )

    @classmethod
    def enter_s(
        cls,
        identifier,
        timestamp = None,
        info = None,
        key = None,
        verify = False
    ):
        info = info or dict()
        if verify: entity.Entity.verify_g(identifier, key)
        enter = cls(
            entity = identifier,
            timestamp = timestamp,
            info = info
        )
        enter.save()
        return enter
