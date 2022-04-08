from app import index


def test_index():
    res = index()
    assert res['id'] == 1