from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_before_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_at_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_at_23_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_at_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_at_27_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_should_have_different_age_after_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_age_for_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
