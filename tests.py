import unittest

from algorytmy_impl import synchronous_stream_cipher
from rsa_implementation import generate_rsa_keys, keysgen, numencrypt


class TestCrypt(unittest.TestCase):
    def test_RSA(self):
        p = 7
        q = 11
        actual = generate_rsa_keys(p, q)
        expected = (77, 65537, 53)
        self.assertEqual(actual, expected)

        pass


    def test_keysgen(self):
        p = 7
        q = 11
        actual = keysgen(p, q)
        expected = {'priv': (53, 77), 'pub': (35537, 77)}
        self.assertEqual(actual, expected)

    def test_numencrypt_encrypt(self):
        priv = (720926705, 982634309)
        pub = (35537, 982634309)
        message = 80087
        actual = numencrypt(message, priv)
        expected = 539186383
        self.assertEqual(actual, expected)

    # def test_numencrypt_decrypt(self):
    #     priv = (720926705, 982634309)
    #     pub = (35537, 982634309)
    #     message = 895887933
    #     actual = numencrypt(message, pub)
    #     expected = 1323123123
    #     self.assertEqual(actual, expected)

