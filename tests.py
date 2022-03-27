import unittest

from algorytmy_impl import synchronous_stream_cipher


class TestCrypt(unittest.TestCase):
    def test_checked_when_synchronous_stream_cipher_is_correct(self):
        text = "Bezpieczeństwo sieci komputerowych"
        state = 6
        input_key = "4-1"
        actual = synchronous_stream_cipher(text, input_key, state, 128)
        expected = "rTK@YTSJUŵBEF_CXTSY[_]ADETB^GHRX"
        self.assertEqual(actual, expected)

    def test2_checked_when_synchronous_stream_cipher_is_correct(self):
        text = "Bezpieczeństwo sieci komputerowych"
        state = 8
        input_key = "5-1"
        actual = synchronous_stream_cipher(text, input_key, state, 128)
        expected = "rUJAYUSKUŴCEG_BYUSX[_\@EDTB_GHSX"
        self.assertEqual(actual, expected)

    def test3_checked_when_decrypt_synchronous_stream_cipher_is_correct(self):
        text = "rTK@XTSKTŴBEG^CXTSX[^\@DEUC^GHRX"
        state = 6
        input_key = "5-3-1"
        actual = synchronous_stream_cipher(text, input_key, state, 128)
        expected = "Bezpieczeństwo sieci komputerowych"
        self.assertEqual(actual, expected)

    def test4_checked_when_decrypt_synchronous_stream_cipher_is_correct(self):
        text = "rTK@XTSKTŴBEG^CXTSX[^\@DEUC^GHRX"
        state = 6
        input_key = "5-3-1"
        actual = synchronous_stream_cipher(text, input_key, state, 128)
        expected = "Bezpieczeństwo sieci komputerowych"
        self.assertEqual(actual, expected)
