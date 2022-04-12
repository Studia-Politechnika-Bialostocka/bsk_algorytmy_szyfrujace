import unittest

from rsa_implementation import encrypt_rsa, decrypt_rsa


class TestCrypt(unittest.TestCase):

    def test_encrypt(self):
        text = 'hello'
        enc_key = (7, 143)
        actual = encrypt_rsa(text, enc_key)
        expected = [91, 62, 4, 4, 45]
        self.assertEqual(actual, expected)

    def test_decrypt(self):
        text = [91, 62, 4, 4, 45]
        dec_key = (223, 143)
        actual = decrypt_rsa(text, dec_key)
        expected = 'hello'
        self.assertEqual(actual, expected)