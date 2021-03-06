# pylint: disable=bad-continuation
from __future__ import unicode_literals
import unittest

from cmake_format.command_tests import TestBase
from cmake_format.parser import NodeType


class TestAddExecutableCommand(TestBase):
  """
  Test various examples of add_executable()
  """

  def test_single_argument(self):
    self.source_str = """\
add_executable(foobar foo.cc)
"""

    self.expect_parse = [
      (NodeType.BODY, [
        (NodeType.STATEMENT, [
          (NodeType.FUNNAME, []),
          (NodeType.LPAREN, []),
          (NodeType.ARGGROUP, [
            (NodeType.PARGGROUP, [
              (NodeType.ARGUMENT, []),
            ]),
            (NodeType.PARGGROUP, [
              (NodeType.ARGUMENT, []),
            ]),
          ]),
          (NodeType.RPAREN, []),
        ]),
        (NodeType.WHITESPACE, []),
      ]),
    ]

    self.expect_format = """\
add_executable(foobar foo.cc)
"""

  def test_all_arguments(self):
    self.source_str = """\
add_executable(foobar WIN32 EXCLUDE_FROM_ALL sourcefile_01.cc
  sourcefile_02.cc sourcefile_03.cc sourcefile_04.cc sourcefile_05.cc
  sourcefile_06.cc sourcefile_07.cc)
"""

    self.expect_parse = [
      (NodeType.BODY, [
        (NodeType.STATEMENT, [
          (NodeType.FUNNAME, []),
          (NodeType.LPAREN, []),
          (NodeType.ARGGROUP, [
            (NodeType.PARGGROUP, [
              (NodeType.ARGUMENT, []),
              (NodeType.FLAG, []),
              (NodeType.FLAG, []),
            ]),
            (NodeType.PARGGROUP, [
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
              (NodeType.ARGUMENT, []),
            ]),
          ]),
          (NodeType.RPAREN, []),
        ]),
        (NodeType.WHITESPACE, []),
      ]),
    ]

    self.expect_format = """\
add_executable(foobar WIN32 EXCLUDE_FROM_ALL
               sourcefile_01.cc
               sourcefile_02.cc
               sourcefile_03.cc
               sourcefile_04.cc
               sourcefile_05.cc
               sourcefile_06.cc
               sourcefile_07.cc)
"""

  def test_sort_arguments(self):
    self.config.autosort = True
    self.source_str = """\
add_executable(foobar WIN32 sourcefile_04.cc
  sourcefile_03.cc sourcefile_01.cc sourcefile_02.cc)
"""

    self.expect_format = """\
add_executable(foobar WIN32
               sourcefile_01.cc
               sourcefile_02.cc
               sourcefile_03.cc
               sourcefile_04.cc)
"""

  def test_disable_autosort_with_tag(self):
    self.config.autosort = True
    self.source_str = """\
add_executable(foobar WIN32 # cmake-format: unsort
  sourcefile_04.cc sourcefile_03.cc sourcefile_01.cc sourcefile_02.cc)
"""

    self.expect_format = """\
add_executable(foobar WIN32
               # cmake-format: unsort
               sourcefile_04.cc
               sourcefile_03.cc
               sourcefile_01.cc
               sourcefile_02.cc)
"""


if __name__ == '__main__':
  unittest.main()
