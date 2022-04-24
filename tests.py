import unittest

from rsa_implementation import encrypt_rsa, decrypt_rsa, gcd, extended_gcd


class TestCrypt(unittest.TestCase):
    def test_encrypt(self):
        text = "hello"
        enc_key = (7, 143)
        actual = encrypt_rsa(text, enc_key)
        expected = [91, 62, 4, 4, 45]
        self.assertEqual(actual, expected)

    def test_decrypt(self):
        text = [91, 62, 4, 4, 45]
        dec_key = (223, 143)
        actual = decrypt_rsa(text, dec_key)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_gcd(self):
        a = 8
        b = 12
        actual = gcd(a, b)
        expected = 4
        self.assertEqual(actual, expected)

    def test_extended_gcd(self):
        a = 8
        b = 12
        actual = extended_gcd(a, b)
        expected = (4, -1, 1)
        self.assertEqual(actual, expected)
