#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import action
from .. import entity

class EntryAction(action.Action):

    entity = appier.field(
        type = appier.reference(
            entity.Entity,
            name = "identifier"
        ),
        observations = """The entity that has just entered
        a certain area of coverage"""
    )

    @classmethod
    def entry_s(cls, entity):
        entry = cls(entity = entity)
        entry.save()
        return entry
