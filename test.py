import unittest

from algorytmy_impl import RF1, RF2


class TestCrypt(unittest.TestCase):
    def test_checked_when_encrypt_rail_fence_is_correct(self):
        cipher = "WEAREDISCOVEREDFLEEATONCE"
        key = 3
        actual = RF1(cipher, key)
        expected = "WECRLTEERDSOEEFEAOCAIVDEN"
        self.assertEqual(actual, expected)

    def test_checked_when_decrypt_rail_fence_is_correct(self):
        cipher = "WECRLTEERDSOEEFEAOCAIVDEN"
        key = 3
        actual = RF2(cipher, key)
        expected = "WEAREDISCOVEREDFLEEATONCE"
        self.assertEqual(actual, expected)
