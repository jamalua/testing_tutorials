import pytest
import sys
from tut3.myapp.sample import add


def test_add_num():
    assert add(1, 2) == 3


@pytest.mark.skip(reason="just want to skip")
def test_add_str():
    assert add("a", "b") == "ab"


@pytest.mark.skipif(sys.version_info > (3, 11), reason="Version greater than 3.7")
def test_add_str2():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "win32", reason="Windows")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
