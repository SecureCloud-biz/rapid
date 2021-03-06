"""
Copyright (c) 2015 Michael Bright and Bamboo HR LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from unittest.case import TestCase

from nose.tools.trivial import eq_

from rapid.testmapper import PythonFile


class TestQaDal(TestCase):

    def test_parse_action(self):
        python_file = PythonFile(None, None)

        eq_("unit", python_file.parse_action("@rapid-unit Test:Test:Testing"))
        eq_("unit", python_file.parse_action("rapid-unit: Test:Test:Testing"))
        eq_(None, python_file.parse_action("@@@@rapid-unit12: Test:Test:Testing"))
