import pytest
from moduls.functions import generate_unique_numbers, input_num


def test_generate_unique_numbers():
    assert len(generate_unique_numbers(9, 1, 90)) == 9


def test_input_num(monkeypatch):
    responses = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    assert input_num() == (2, 1)

