import pytest
from modules.profile_fetcher2 import ProfileFetch


def search(query):
    obj = ProfileFetch()
    return obj.fb_profile_fetch(query)


@pytest.mark.parametrize("id", ['100000143127056', 'priscilla'])
def test_profile_fetch(id):
    res = search(id)
    try:
        assert isinstance(res['name'], str)
        assert res['name'] != ""
    except:
        assert res['name'] is None

    try:
        assert isinstance(res['profile_image'], str)
        assert res['profile_image'] != ""
        assert res['profile_image'].startswith('http')
    except:
        assert res['profile_image'] is None

    try:
        assert isinstance(res['profile_url'], str)
        assert res['profile_url'] != ""
        assert res['profile_url'].startswith('http')
    except:
        assert res['profile_url'] is None