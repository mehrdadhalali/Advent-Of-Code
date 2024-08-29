from day_2 import extract_dimensions, calculate_areas, calculate_paper_needed_per_gift
from day_2 import calculate_total_paper_needed


def test_extract_dimensions():

    assert extract_dimensions("12x5x1") == (12, 5, 1)
    assert extract_dimensions("45x99x8324") == (45, 99, 8324)


def test_calculate_areas():

    assert calculate_areas(2, 3, 4) == [6, 12, 8]
    assert calculate_areas(1, 1, 10) == [1, 10, 10]


def test_calculate_paper_needed_per_gift():

    assert calculate_paper_needed_per_gift(2, 3, 4) == 58
    assert calculate_paper_needed_per_gift(1, 1, 10) == 43


def test_calculate_total_paper_needed():

    assert calculate_total_paper_needed([(2, 3, 4), (1, 1, 10)]) == 101
