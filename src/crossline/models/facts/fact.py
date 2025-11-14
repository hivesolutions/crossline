#!/usr/bin/python
# -*- coding: utf-8 -*-

from .. import base
from .. import mixins


class Fact(base.CrosslineBase, mixins.Day):
    """
    The abstract model class that represents a fact,
    should provide the infra-structure to easy the
    usage and exploration of facts.
    """

    @classmethod
    def is_abstract(cls):
        return True
