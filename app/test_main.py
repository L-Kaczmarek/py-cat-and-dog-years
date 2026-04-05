from app.main import get_human_age


def test_get_human_age_less_then_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_beetween_15_27() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_more_than_27() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
