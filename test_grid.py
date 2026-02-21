from grid import gridChallenge


def test_grid_yes_simple():

    grid = ["abc", "bcd", "cde"]

    assert gridChallenge(grid) == "YES"


def test_grid_yes_sorting():

    grid = ["cba", "daf", "ghi"]

    assert gridChallenge(grid) == "YES"


def test_grid_no():

    grid = ["zxy", "wvu", "tsr"]

    assert gridChallenge(grid) == "NO"