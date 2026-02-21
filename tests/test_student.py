from student_system.student import Student


def test_get_grade_A():
    s = Student("Tom", 90)
    assert s.get_grade() == "A"


def test_get_grade_B():
    s = Student("Tom", 80)
    assert s.get_grade() == "B"


def test_get_grade_C():
    s = Student("Tom", 60)
    assert s.get_grade() == "C"


def test_get_grade_F():
    s = Student("Tom", 59.9)
    assert s.get_grade() == "F"