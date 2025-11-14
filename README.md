# [Crossline](http://crossline.hive.pt)

Simple event pipping and storing infra-structure to be for crossing, entering and other events.

## Adapters

There's currently three adapters for the Crossline infra-structure:

| Name           | Description                                                                            |
| -------------- | -------------------------------------------------------------------------------------- |
| `LocalAdapter` | For local data source storage of information.                                          |
| `OmniAdapter`  | For the push of information from the Crossline to an Omni instance for warehousing.    |
| `PicaAdapter`  | To enable integration of enter operation in [PicaPonto](https://picaponto.pt) service. |

## Configuration

| Name              | Type  | Default                 | Description                                                                                                                                                              |
| ----------------- | ----- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **LOCAL_ENABLED** | `str` | `True`                  | If the Local adapter is enabled.                                                                                                                                         |
| **OMNI_ENABLED**  | `str` | `True`                  | If the Onni adapter is enabled, notice that additional values are required to make the adapter ready.                                                                    |
| **PICA_ENABLED**  | `str` | `True`                  | If the [PicaPonto](https://picaponto.pt) adapter is enabled, notice that additional requirements (eg: company definitions) may apply to properly make the adapter ready. |
| **PICA_BASE_URL** | `str` | `https://picaponto.pt/` | The base URL to access [PicaPonto](https://picaponto.pt).                                                                                                                |
| **PICA_COMPANY**  | `int` | `None`                  | The identifier of [PicaPonto](https://picaponto.pt) company associated.                                                                                                  |

## License

Crossline is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://github.com/hivesolutions/crossline/workflows/Main%20Workflow/badge.svg)](https://github.com/hivesolutions/crossline/actions)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/crossline/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/crossline?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/crossline.svg)](https://pypi.python.org/pypi/crossline)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
