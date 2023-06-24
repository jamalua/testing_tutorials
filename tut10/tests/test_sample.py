from unittest import mock
from tut10.myapp.sample import random_sum


@mock.patch("tut10.myapp.sample.random.randint")
def test_random_sum(mock_random_int):
    mock_random_int.side_effect = [3, 4]
    assert random_sum() == 7
