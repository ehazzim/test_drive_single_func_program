from lib.estimate_reading_time import estimate_reading_time
import pytest

def test_empty_string():
    empty_string = estimate_reading_time("")
    assert empty_string == 0

def test_exactly_200():
    text = "word " * 200
    exact_amount = estimate_reading_time(text)
    assert exact_amount == 1.0

def test_400_words():
    text = "word " * 400
    exact_amount = estimate_reading_time(text)
    assert exact_amount == 2.0

def test_300_words():
    text = "word " * 300
    exact_amount = estimate_reading_time(text)
    assert exact_amount == 1.5

def test_input_type():
    with pytest.raises(Exception) as e:
        estimate_reading_time(123)
    error_message = str(e.value)
    assert error_message == "This needs to be a string!"