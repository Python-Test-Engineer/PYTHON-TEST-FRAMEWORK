from datetime import datetime

from tut7.myapp.student import get_topper


def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("shyam", 19),
        make_dummy_student("ravi", 22),
    ]

    topper = get_topper(students)

    assert topper == students[2]
