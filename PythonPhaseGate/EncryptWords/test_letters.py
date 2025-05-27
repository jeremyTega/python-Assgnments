import function_encrypy
import unittest

class TestEncryptText(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(function_encrypy.encrypt("hello world"), "uryyb jbeyq")

    def test_uppercase_letters(self):
        self.assertEqual(function_encrypy.encrypt("HELLO WORLD"), "URYYB JBEYQ")

    def test_mixed_letters(self):
        self.assertEqual(function_encrypy.encrypt("Hello World"), "Uryyb Jbeyq")
