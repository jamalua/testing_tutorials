import json
import os
from tut5.myapp.sample import save_dict


def test_save_dict(tempdir):
    filepath = os.path.join(tempdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
