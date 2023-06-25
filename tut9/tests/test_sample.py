from unittest import mock
import pytest

from tut9.myapp.sample import guess_number, get_ip


@pytest.mark.parametrize("_input, expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("tut9.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected


@mock.patch("tut9.myapp.sample.requests.get")
def test_get_ip(mock_requst_get):
    response_mock = mock.Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {"origin": "0.0.0.0"}
    mock_requst_get.return_value = response_mock
    assert get_ip() == "0.0.0.0"
