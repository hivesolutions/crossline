#!/usr/bin/python
# -*- coding: utf-8 -*-

import crossline.adapters

ADAPTERS = (
    crossline.adapters.BaseAdapter,
    crossline.adapters.OmniAdapter
)
""" The sequence defining the complete set of adapter
classes that may be used for runtime notification """

def get_adapters():
    adapters = []
    for adapter_c in ADAPTERS:
        if not adapter_c.ready(): continue
        adapter = adapter_c()
        adapters.append(adapter)
    return adapters
