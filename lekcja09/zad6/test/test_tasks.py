from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest

from src.anagram import they_are_anagrams
from src.palindrome import is_palindrome
from src.pattern_search import search_pattern_in_text
from test.test_logger import TestLogger


class TasksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results()

    def test_should_recognize_that_strings_are_anagrams(self):
        s1 = 'karol'
        s2 = 'rolka'
        result = they_are_anagrams(s1, s2)
        TasksTest.logger.log_single_test_result("test_should_recognize_that_strings_are_anagrams", result == True)
        self.assertEqual(True, result)

    def test_should_recognize_that_strings_are_not_anagrams(self):
        s1 = 'this'
        s2 = 'that'
        result = they_are_anagrams(s1, s2)
        TasksTest.logger.log_single_test_result("test_should_recognize_that_strings_are_not_anagrams", result == False)
        self.assertEqual(False, result)

    def test_should_recognize_that_string_is_palindrome(self):
        s = 'kajak'
        result = is_palindrome(s)
        TasksTest.logger.log_single_test_result("test_should_recognize_that_string_is_palindrome", result == True)
        self.assertEqual(True, result)

    def test_should_recognize_that_string_is_not_palindrome(self):
        s = 'kajaki'
        result = is_palindrome(s)
        TasksTest.logger.log_single_test_result("test_should_recognize_that_string_is_not_palindrome", result == False)
        self.assertEqual(False, result)

    def test_should_recognize_pattern_in_string_at_correct_position(self):
        string = 'lokomotywa'
        pattern = 'motyw'
        result = search_pattern_in_text(pattern, string)
        TasksTest.logger.log_single_test_result("test_should_recognize_pattern_in_string_at_correct_position",
                                                result == 5)
        self.assertEqual(5, result)

    def test_should_not_recognize_pattern_in_string(self):
        string = 'lokomotywa'
        pattern = 'motywy'
        result = search_pattern_in_text(pattern, string)
        TasksTest.logger.log_single_test_result("test_should_not_recognize_pattern_in_string",
                                                result == -1)
        self.assertEqual(-1, result)


if __name__ == '__main__':
    unittest.main()
