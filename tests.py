import unittest

from rsa_implementation import encrypt_rsa, decrypt_rsa, gcd, getKeys


class TestCrypt(unittest.TestCase):
    def test_encrypt(self):
        text = "hello"
        enc_key, desc_key = getKeys(11, 13)
        actual = encrypt_rsa(text, enc_key)
        expected = [91, 62, 4, 4, 45]

        self.assertEqual(actual, expected)

    def test_decrypt(self):
        text = [91, 62, 4, 4, 45]
        enc_key, dec_key = getKeys(11, 13)
        actual = decrypt_rsa(text, dec_key)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_encrypt1(self):
        text = "baba"
        enc_key, desc_key = getKeys(11, 13)
        actual = encrypt_rsa(text, enc_key)
        expected = [32,59,32,59]

        self.assertEqual(actual, expected)

    def test_decrypt1(self):
        text = [32,59,32,59]
        enc_key, dec_key = getKeys(11, 13)
        actual = decrypt_rsa(text, dec_key)
        expected = "baba"
        self.assertEqual(actual, expected)

    def test_encrypt2(self):
        text = "baba"
        enc_key, desc_key = getKeys(17, 13)
        actual = encrypt_rsa(text, enc_key)
        expected = [115,54,115,54]

        self.assertEqual(actual, expected)

    def test_decrypt2(self):
        text = [115,54,115,54]
        enc_key, dec_key = getKeys(17, 13)
        actual = decrypt_rsa(text, dec_key)
        expected = "baba"
        self.assertEqual(actual, expected)

    def test_gcd(self):
        a = 8
        b = 12
        actual = gcd(a, b)
        expected = 4
        self.assertEqual(actual, expected)

