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
        return ["created", "entity", "app"]

    @classmethod
    def enter_s(cls, identifier, key = None, verify = False):
        if verify: entity.Entity.verify_g(identifier, key)
        enter = cls(entity = identifier)
        enter.save()
        return enter
