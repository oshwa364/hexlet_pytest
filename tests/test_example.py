from hexlet_pytest.example import reverse, change
import pytest


def test_reverse():
    print('HELLO!')
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''

@pytest.fixture()
def collection():
    return[1, 2, 3, 4]


def test_change(collection):
    change(collection)
    assert collection == [2, 3, 4, 5]
    print(collection)
    change(collection)
    assert collection == [3, 4, 5, 6]
    print(collection)

def test_change2(collection):
    change(collection)
    assert collection == [2, 3, 4, 5]
    print(collection)