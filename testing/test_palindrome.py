from unittest import TestCase
from testing.palindrome import check_palindrome

class TestCheckPalindrome(TestCase):
    def test_correct_palindrome(self):
        result = check_palindrome("Racecar")
        self.assertEqual(result, True)

    def not_palindrome(self):
        result = check_palindrome("cat")
        self.assertEqual(result, False)

    def empty(self):
        result = check_palindrome("")
        self.assertEqual(result, True)