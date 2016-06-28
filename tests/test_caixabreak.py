#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_caixabreak
----------------------------------

Tests for `caixabreak` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from caixabreak import caixabreak


class TestCaixabreak(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        help_result = runner.invoke(caixabreak.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
