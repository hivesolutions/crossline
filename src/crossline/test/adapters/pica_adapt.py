#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import logging
import unittest

import appier

import crossline

class PicaAdaptTest(unittest.TestCase):

    def setUp(self):
        self.app = crossline.CrosslineApp(level = logging.ERROR)

    def tearDown(self):
        self.app.unload()
        adapter = appier.get_adapter()
        adapter.drop_db()

    def test_basic(self):
        pica_adapt = crossline.PicaAdapter()

        crossline.Entity.create_s("username")

        result = pica_adapt._res_movement("username")
        self.assertEqual(result, "Entrada")

        crossline.EnterAction.enter_s("username", timestamp = int(time.time() - 3600))

        result = pica_adapt._res_movement("username")
        self.assertEqual(result, "Saída")

        crossline.EnterAction.enter_s("username", info = {"pica:movimento": "Saída"})

        result = pica_adapt._res_movement("username")
        self.assertEqual(result, "Duplicado")

        result = pica_adapt._res_movement(
            "username",
            timestamp = int(time.time() + crossline.PicaAdapter.DUPLICATE_THRESHOLD + 1)
        )
        self.assertEqual(result, "Entrada")

        crossline.EnterAction.enter_s("username", info = {"pica:movimento": "Entrada"})

        result = pica_adapt._res_movement(
            "username",
            timestamp = int(time.time() + crossline.PicaAdapter.DUPLICATE_THRESHOLD + 1)
        )
        self.assertEqual(result, "Saída")

        result = pica_adapt._res_movement(
            "username",
            timestamp = int(time.time() + crossline.PicaAdapter.TURN_THRESHOLD + 1)
        )
        self.assertEqual(result, "Entrada")
