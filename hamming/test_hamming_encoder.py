import unittest
import hamming_encoder


class TestHammingEncoder(unittest.TestCase):

    def test_non_binary_number(self):
        hamming_even = hamming_encoder.HammingEncoder()
        result = hamming_even.encode(234123)
        self.assertEqual(result, -1)

    def test_list_with_non_binary_numbers(self):
        hamming_even = hamming_encoder.HammingEncoder()
        result = hamming_even.encode([1, 1, 2, 0])
        self.assertEqual(result, -1)

    def test_list_len_not_eleven_return_minus_one(self):
        hamming_even = hamming_encoder.HammingEncoder()
        result = hamming_even.encode([1, 1, 0, 0])
        self.assertEqual(result, -1)

    def test_encoder_default_should_be_even(self):
        hamming_even = hamming_encoder.HammingEncoder()
        result = hamming_even.encode([1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
        self.assertEqual(result, [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0])

    def test_encoder_can_receive_numbers(self):
        hamming_even = hamming_encoder.HammingEncoder()
        result = hamming_even.encode(11001001010)
        self.assertEqual(result, [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0])

    def test_encode_even(self):
        hamming_even = hamming_encoder.HammingEncoder(hamming_encoder.Parity.EVEN)
        result = hamming_even.encode([1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
        self.assertEqual(result, [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0])

    def test_encode_odd(self):
        hamming_even = hamming_encoder.HammingEncoder(hamming_encoder.Parity.ODD)
        result = hamming_even.encode([1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
        self.assertEqual(result, [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
