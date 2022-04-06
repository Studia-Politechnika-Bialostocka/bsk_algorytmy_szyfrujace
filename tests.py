import unittest

from algorytmy_impl import synchronous_stream_cipher
from rsa_implementation import makeKeyFiles


class TestCrypt(unittest.TestCase):


    def test_makeKeyFiles(self):
        file_name = "RSA_demo"
        key_size = 8
        actual = makeKeyFiles(file_name, key_size)
        expected = True
        self.assertEqual(actual, expected)
