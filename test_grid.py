from grid import gridChallenge


def test_grid_yes():

    grid = ["abc", "bcd", "cde"]

    assert gridChallenge(grid) == "YES"


def test_grid_no():

    grid = ["cba", "daf", "ghi"]

    assert gridChallenge(grid) == "NO"