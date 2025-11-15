import pytest
from sorts import qsort


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        (
            [-1466, -1612, -1174, -9929, 7321, -6372, 6576],
            [-9929, -6372, -1612, -1466, -1174, 6576, 7321],
        ),
        (
            [7208, 9672, 1748, -537, 7092, -717, 5356, 8352],
            [-717, -537, 1748, 5356, 7092, 7208, 8352, 9672],
        ),
        ([-7194, -757], [-7194, -757]),
        ([-1161, 8675, 1323, 5628, 2318], [-1161, 1323, 2318, 5628, 8675]),
        ([-8407, 4518, 3782, -4880], [-8407, -4880, 3782, 4518]),
    ],
)
def test_qsort_true(arr, expected):
    assert qsort(arr) == expected


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([9, 9, 9, 9], [9, 9, 9, 9]),
        ([10000], [10000]),
    ],
)
def test_edge_cases_qsort(arr, expected):
    assert qsort(arr) == expected


def property_based_qsort(generated_list):
    for _ in range(1000):
        sorted_arr = qsort(generated_list)
        expected = sorted(generated_list)

        assert len(sorted_arr) == len(expected)
        assert sorted_arr == expected
