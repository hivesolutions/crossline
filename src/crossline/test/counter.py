#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

import appier

import crossline

class CounterTest(unittest.TestCase):

    def setUp(self):
        self.app = crossline.CrosslineApp(level = logging.ERROR)

    def tearDown(self):
        self.app.unload()
        adapter = appier.get_adapter()
        adapter.drop_db()

    def test_basic(self):
        counter = crossline.CounterFact.increment_s(app = "test")

        self.assertEqual(counter, 1)

        facts = crossline.CounterFact.find()

        self.assertEqual(len(facts), 1)
        self.assertEqual(facts[0].counter, 1)
