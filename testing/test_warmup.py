#BOILER PLATE
from unittest import TestCase
from testing.warmup import other_string_split
from testing.warmup import string_split

#to test you need to have written a function
#
# class meaningful_name(TestCase): #name of function, class or file you're testing for prefaced with name test
#     #e.g. TestCaseSplit(TestCase)  -- all classes need to start with capital letter
#     pass

class TestOtherStringSplit(TestCase): #will pass the test
    def test_normal_string(self):
        result = other_string_split("Sally")
        expected_result = "S-a-l-l-y"
        self.assertEqual(result, expected_result)

class TestStringSplit(TestCase): #will not pass the test
    def test_normal_string(self):
        result = string_split("Sally")
        expected_result = "S-a-l-l-y"
        self.assertEqual(result, expected_result)


