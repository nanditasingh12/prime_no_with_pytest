import pytest
from prime import is_prime, first_100_primes

def test_first_100_primes_length():
    primes = first_100_primes()
    assert len(primes) == 100  # Should pass

def test_all_are_prime():
    for p in first_100_primes():
        assert is_prime(p)  # Should pass

def test_known_prime():
    assert is_prime(7) == True  # Should pass

def test_known_non_prime():
    assert is_prime(4) == False  # Should pass

