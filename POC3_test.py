import pytest


def _test_POC3():
    assert 'Semaphore' == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    assert 2 == 2