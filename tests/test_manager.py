from student_system.manager import StudentManager


def test_add_student_new():
    m = StudentManager()
    m.add_student("Tom", 90)

    s = m.find_student("Tom")
    assert s is not None
    assert s.score == 90


def test_add_student_update_existing():
    m = StudentManager()
    m.add_student("Tom", 90)
    m.add_student("Tom", 95)  # update

    s = m.find_student("Tom")
    assert s.score == 95


def test_delete_student():
    m = StudentManager()
    m.add_student("Tom", 90)

    ok = m.delete_student("Tom")
    assert ok is True
    assert m.find_student("Tom") is None


def test_top_n():
    m = StudentManager()
    m.add_student("A", 60)
    m.add_student("B", 80)
    m.add_student("C", 90)

    top2 = m.top_n(2)
    assert len(top2) == 2
    assert top2[0].name == "C"
    assert top2[1].name == "B"