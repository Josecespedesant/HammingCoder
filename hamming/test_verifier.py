import pytest
from hamming_verifier import HammingVerifier, is_binary


@pytest.mark.parametrize(
    "string, is_even, expected",
    [
        ("101010011001010", True, 4),
        ("110101101001010", True, 13),
        ("000001101001110", False, 8),
        ("101101001010111", False, 1)
    ]
)
def test_verifier(string, is_even, expected):
    position = HammingVerifier().check_parity(string, is_even)
    assert position == expected


@pytest.mark.parametrize(
    "string, is_even",
    [
        ("101010011", True),
        ("110101101001010001010", True),
        ("00000110100111001", False),
        ("101", False)
    ]
)
def test_wrong_length_returns_minus_one(string, is_even):
    position = HammingVerifier().check_parity(string, is_even)
    assert position == -1


@pytest.mark.parametrize(
    "string",
    [
        "101010011071010",
        "118",
        "000001101081110",
        "101101001040111"
    ]
)
def test_non_binary_string_returns_false(string):
    assert is_binary(string) == False

@pytest.mark.parametrize(
    "string",
    [
        "10101001101010",
        "11",
        "000001101001000100010101100101011110",
        "101101001010101001100110100111"
    ]
)
def test_binary_string_returns_true(string):
    assert is_binary(string) == True