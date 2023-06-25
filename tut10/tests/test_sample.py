from unittest import mock
from tut10.myapp.sample import random_sum, silly


@mock.patch("tut10.myapp.sample.random.randint")
def test_random_sum(mock_random_int):
    mock_random_int.side_effect = [3, 4]
    assert random_sum() == 7


@mock.patch("tut10.myapp.sample.random.randint")
@mock.patch("tut10.myapp.sample.time.time")
@mock.patch("tut10.myapp.sample.requests.get")
def test_silly(mock_request_get, mock_time, mock_random_int):
    test_params = {
        "timestamp": 100,
        "number": 4,
    }
    mock_time.return_value = 100
    mock_random_int.return_value = 4
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"args": {"timestamp": 100, "number": 4}}
    mock_request_get.return_value = mock_response
    assert silly() == test_params
