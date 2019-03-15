from modules.fb_post_search import PostSearch
import pytest


def search(q):
    obj = PostSearch()
    return obj.fb_posts(q)


@pytest.mark.parametrize("query", ['trump', 'Nguyễn Phú Trọng'])
def test_post_search(query):
    res = search(query)
    for i in res:

        assert isinstance(i['datetime'], int)
        assert isinstance(i['likes'], int)
        assert isinstance(i['shares'], int)
        assert isinstance(i['comments'], int)
        # assert isinstance(i['polarity'], str)
        # assert i['polarity'] == 'neutral' or 'positive' or 'negative'

        try:
            # check for url
            assert isinstance(i['url'], str)
            assert i['url'].startswith('http')
        except AssertionError:
            assert i['url'] is None

        try:
            assert isinstance(i['thumbnail'], str)
            assert i['thumbnail'].startswith('http')
        except AssertionError:
            assert i['thumbnail'] is None

        try:
            # check for url
            assert isinstance(i['author_image'], str)
            assert i['author_image'].startswith('http')
        except AssertionError:
            assert i['author_image'] is None

        try:
            # check for non empty string
            assert isinstance(i['content'], str)
            assert i['content'] != ''
        except AssertionError:
            assert i['content'] is None

        try:
            # check for non empty string
            assert isinstance(i['author_name'], str)
            assert i['author_name'] != ''
        except AssertionError:
            assert i['author_name'] is None

        try:
            # check for non empty string
            assert isinstance(i['author_userid'], str)
            assert i['author_userid'] != ''
            assert ' ' not in i['author_userid']
        except AssertionError:
            assert i['author_userid'] is None

        assert i['type'] == 'image' or i['type'] == 'video' or i['type'] == 'status'






