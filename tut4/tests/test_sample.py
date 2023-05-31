from tut4.myapp.sample import add
import pytest


@pytest.mark.parametrize(
    "first, second, result",
    [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])],
    ids=["num", "string", "list"],
)
def test_add(first, second, result):
    assert add(first, second) == result
