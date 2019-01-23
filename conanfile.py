#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostCrcConan(base.BoostBaseConan):
    name = "boost_crc"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_crc"
    lib_short_names = ["crc"]
    header_only_libs = ["crc"]
    b2_requires = [
        "boost_config",
        "boost_integer",
    ]


