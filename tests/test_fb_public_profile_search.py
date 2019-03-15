from modules.fb_public_profile_search import ProfileSearch
import pytest


def search(name):
    obj = ProfileSearch()
    return obj.fb_public_search(name)


@pytest.mark.parametrize("query", ['trump', 'Nguyễn Phú Trọng'])
def test_public_profile_search(query):
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
            assert type(i['userid']) == str
            assert i['userid'] != ""
        except:
            assert i['userid'] is None

        try:
            assert i['image'] != ""
            assert type(i['image']) == str
            assert i['image'].startswith('http')
        except:
            assert i['image'] is None

        assert type(i['verified']) == bool
        # assert isinstance(i['verified'], bool)

        assert i['type'] is 'identity'



