from datetime import datetime
from tut7.myapp.student import Student, get_topper


def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student


def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 12),
        make_dummy_student("shyam", 19),
        make_dummy_student("ravi", 22),
    ]

    topper = get_topper(students)

    assert topper == students[2]
