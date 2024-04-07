from project import get_date, get_month_num, get_month_name
import pytest
from datetime import date

def test_get_date():
    assert get_date("2005-06-10") == date(2005, 6, 10)
    with pytest.raises(ValueError):
        get_date("difd893fjdk")

def test_get_month_num():
    assert get_month_num("June") == 6
    assert get_month_num("January") == 1
    with pytest.raises(ValueError):
        get_month_num("jsdkfjks")

def test_get_month_name():
    assert get_month_name(3) == "March"
    with pytest.raises(IndexError):
        get_month_name(13)