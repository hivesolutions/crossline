#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name = "crossline",
    version = "0.1.0",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Crossline System",
    license = "Apache License, Version 2.0",
    keywords = "crossline, control, cameras",
    url = "http://crossline.hive.pt",
    zip_safe = False,
    packages = [
        "crossline",
        "crossline.controllers",
        "crossline.models",
        "crossline.util"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    install_requires = [
        "appier",
        "appier_extras",
        "omni_api"
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
