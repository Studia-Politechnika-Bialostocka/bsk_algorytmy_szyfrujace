import unittest

from algorytmy_impl import RF1, RF2, PM2, PM2_decrypt, PM, PM_decrypt


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

    def test_checked_when_encrypt_matrix_conversion1_is_correct(self):
        cipher = "CRYPTOGRAPHYOSA"
        key = "3-4-1-5-2"
        actual = PM2(cipher, key)
        expected = "RH PO OA R TS A CP YY G "
        self.assertEqual(actual, expected)

    def test_checked_when_decrypt_matrix_conversion1_is_correct(self):
        cipher = "RH PO OA R TS A CP YY G "
        key = "3-4-1-5-2"
        actual = PM2_decrypt(cipher, key)
        expected = "CRYPTOGRAPHYOSA"
        self.assertEqual(actual, expected)

    def test_checked_when_encrypt_matrix_conversion_is_correct(self):
        cipher = "POLITECHNIKA"
        d = 5
        key = [3, 4, 1, 5, 2]
        actual = PM(cipher, d, key)
        expected = "LIPTOHNEICKA"
        self.assertEqual(actual, expected)

    def test_checked_when_decrypt_matrix_conversion_is_correct(self):
        cipher = "LIPTOHNEICKA"
        d = 5
        key = [3, 4, 1, 5, 2]
        actual = PM_decrypt(cipher, d, key)
        expected = "POLITECHNIKA"
        self.assertEqual(actual, expected)