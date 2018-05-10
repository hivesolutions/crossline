#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

import appier

from . import base

class Entity(base.CrosslineBase):
    """
    Top level class that describes an element that can be
    identifiable under the system as an entity.

    Can be used for operations of control, authentication, etc.
    """

    identifier = appier.field(
        index = "hashed",
        immutable = True
    )

    key = appier.field(
        index = "hashed",
        immutable = True
    )

    @classmethod
    def validate(cls):
        return super(Entity, cls).validate() + [
            appier.not_null("identifier"),
            appier.not_empty("identifier"),
            appier.is_lower("identifier"),
            appier.string_gt("identifier", 3),
            appier.string_lt("identifier", 64),
            appier.not_duplicate("identifier", cls._name()),
        ]

    @classmethod
    def list_names(cls):
        return ["identifier", "key", "app"]

    @classmethod
    def _plural(cls):
        return "Entities"

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        self.key = self.secret(hash = hashlib.md5)
