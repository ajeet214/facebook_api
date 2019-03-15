from modules.fb_public_page_search import PageSearch
import pytest


def search(name):
    obj = PageSearch()
    return obj.fb_page_search(name)


@pytest.mark.parametrize("query", ['trump','Nguyễn Phú Trọng'])
def test_public_page_search(query):
    res = search(query)
    for i in res:

        try:
            assert type(i['url']) == str
            assert i['url'].startswith('http')
            assert i['url'] != ""
        except:
            assert i['url'] is None

        try:
            assert i['description'] != ""
            assert type(i['description']) == str
        except:
            assert i['description'] is None


        try:
            assert type(i['name']) == str
            assert i['name'] != ""
        except:
            assert i['name'] is None


        try:
            assert type(i['location']) == str
            assert i['location'] != ""
        except:
            assert i['location'] is None

        try:
            assert type(i['country']) == str
            assert i['country'] != ""
        except:
            assert i['country'] is None

        try:
            assert type(i['category']) == str
            assert i['category'] != ""
        except:
            assert i['category'] is None

        try:
            assert type(i['country_code']) == str
            assert i['country_code'] != ""
            assert len(i['country_code']) == 2
        except:
            assert i['country_code'] is None

        try:
            assert i['image'] != ""
            assert type(i['image']) == str
            assert i['image'].startswith('http')
        except:
            assert i['image'] is None

        assert type(i['verified']) == bool

        try:
            assert isinstance(i['likes'], int)
        except:
            assert i['likes'] is None

        assert i['type'] is 'page'

