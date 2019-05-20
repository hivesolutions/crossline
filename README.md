# [Crossline](http://crossline.hive.pt)

Simple event pipping and storing infra-structure to be for crossing, entering and other events.

## Adapters

There's currently three adapters for the Crossline infra-structure:

| Name | Description |
| ----- | ----- |
| `LocalAdapter` | For local data source storage of information. |
| `OmniAdapter` | For the push of information from the Crossline to an Omni instance for warehousing. |
| `PicaAdapter` |  To enable integration of enter operation in [PicaPonto](https://picaponto.pt) service. |

## Configuration

| Name | Type | Description |
| ----- | ----- | ----- |
| **PICA_BASE_URL** | `str` | The base URL to access [PicaPonto](https://picaponto.pt) (defaults to `https://picaponto.pt/`).
| **PICA_COMPANY** | `int` | The identifier of [PicaPonto](https://picaponto.pt) company associated (defaults to `None`).

## License

Crossline is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/crossline.svg?branch=master)](https://travis-ci.org/hivesolutions/crossline)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/crossline/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/crossline?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/crossline.svg)](https://pypi.python.org/pypi/crossline)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
