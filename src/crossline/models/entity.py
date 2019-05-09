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
        default = True,
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
    def get_by_id(cls, identifier, app = None):
        return cls.get(identifier = identifier, app = None)

    @classmethod
    @appier.operation(
        name = "Verify",
        parameters = (
            ("Identifier", "identifier", str),
            ("Key", "key", str),
            ("App", "app", str, None)
        )
    )
    def verify_g(cls, identifier, key, app = None):
        entity = cls.get(identifier = identifier, app = app)
        appier.verify(
            entity.key == key,
            message = "Missmatch in key"
        )

    @classmethod
    @appier.operation(
        name = "Create",
        parameters = (("Identifier", "identifier", str),),
        factory = True
    )
    def create_s(cls, identifier):
        entity = cls(identifier = identifier)
        entity.save()
        return entity

    @classmethod
    def _plural(cls):
        return "Entities"

    def pre_create(self):
        base.CrosslineBase.pre_create(self)
        self.key = self.secret(hash = hashlib.md5)

    @appier.operation(
        name = "Set PicaPonto.pt",
        parameters = (
            ("Code", "code", int),
            ("Secret", "secret", int)
        )
    )
    def set_pica_s(self, code, secret):
        self.meta["pica:codigo"] = code
        self.meta["pica:senha"] = secret
        self.save()

    @appier.view(name = "Enter Actions")
    def enter_actions_v(self, *args, **kwargs):
        from .actions import enter
        kwargs["sort"] = kwargs.get("sort", [("timestamp", -1)])
        kwargs.update(entity = self.identifier)
        return appier.lazy_dict(
            model = enter.EnterAction,
            kwargs = kwargs,
            entities = appier.lazy(lambda: enter.EnterAction.find(*args, **kwargs)),
            page = appier.lazy(lambda: enter.EnterAction.paginate(*args, **kwargs))
        )
