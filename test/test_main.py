import pytest


@pytest.mark.parametrize("x,y,res",
                         [
                             (2, 2, 4),
                             (4, 4, 8)
                         ])
def test_main_1(x, y, res):
    assert x+y == res
