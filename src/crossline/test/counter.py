#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import datetime
import unittest

import appier

import crossline


class CounterTest(unittest.TestCase):

    def setUp(self):
        self.app = crossline.CrosslineApp(level=logging.ERROR)

    def tearDown(self):
        self.app.unload()
        adapter = appier.get_adapter()
        adapter.drop_db()

    def test_basic(self):
        current = datetime.datetime.utcnow()

        counter = crossline.CounterFact.increment_s(app="test", current=current)

        self.assertEqual(counter["action"], "cross")
        self.assertEqual(counter["count"], 1)
        self.assertEqual(counter["app"], "test")

        facts = crossline.CounterFact.find()

        self.assertEqual(len(facts), 1)
        self.assertEqual(facts[0].app, "test")
        self.assertEqual(facts[0].counter, 1)

        counter = crossline.CounterFact.increment_s(app="test", current=current)

        self.assertEqual(counter["action"], "cross")
        self.assertEqual(counter["count"], 2)
        self.assertEqual(counter["app"], "test")

        facts = crossline.CounterFact.find()

        self.assertEqual(len(facts), 1)
        self.assertEqual(facts[0].app, "test")
        self.assertEqual(facts[0].counter, 2)

        counter = crossline.CounterFact.increment_s(app="other", current=current)

        facts = crossline.CounterFact.find(sort=[("app", -1)])

        self.assertEqual(len(facts), 2)
        self.assertEqual(facts[0].app, "test")
        self.assertEqual(facts[1].app, "other")
        self.assertEqual(facts[0].counter, 2)
        self.assertEqual(facts[1].counter, 1)
