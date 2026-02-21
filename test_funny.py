from funny import funnyString


def test_funny_true():

    assert funnyString("acxz") == "Funny"


def test_funny_false():

    assert funnyString("bcxz") == "Not Funny"