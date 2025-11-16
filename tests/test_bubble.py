import pytest
from sorts import bubblesort
from generate_list_conf import generated_list

@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        ([1, 5, 7, 1, 21], [1, 1, 5, 7, 21]),
        ([8, 5, 4, 90, 21], [4, 5, 8, 21, 90]),
        ([4, 5, 8, 12], [4, 5, 8, 12]),
    ],
)
def test_bubblesort(arr, expected):
    assert bubblesort(arr) == expected


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        ([-10], [-10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([90, 80, 70, 60, 50, 40], [40, 50, 60, 70, 80, 90]),
        ([], []),
    ],
)
def test__edge_cases_bubblesort(arr, expected):
    assert bubblesort(arr) == expected




def test_property_based_bubblesort():
    for _ in range(1000):
        arr = generated_list()
        sorted_arr = bubblesort(arr)
        expected = sorted(arr)

        assert len(sorted_arr) == len(expected)
        assert sorted_arr == expected
