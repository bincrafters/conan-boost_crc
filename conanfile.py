#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostCrcConan(base.BoostBaseConan):
    name = "boost_crc"
    url = "https://github.com/bincrafters/conan-boost_crc"
    lib_short_names = ["crc"]
    header_only_libs = ["crc"]
    b2_requires = [
        "boost_array",
        "boost_config",
        "boost_integer",
        "boost_type_traits"
    ]
