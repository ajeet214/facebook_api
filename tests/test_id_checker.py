from modules.Id_checker import EmailNumberChecker
import pytest


def search(query):
    obj = EmailNumberChecker()
    return obj.Checker(query)


@pytest.mark.parametrize("number", ['917726933451', '917726933452'])
def test_id_checker(number):
    res = search(number)
    assert type(res['profileExists']) == bool
