import pytest
from sorts import mergesort
from generate_list_conf import generated_list

@pytest.mark.parametrize(
    ["arr","expected"],
    [
       ([6557],[6557]),
    ([9472, 8555, 6973, 7200, 8532, -6347, 9269, 8464, -745],[-6347, -745, 6973, 7200, 8464, 8532, 8555, 9269, 9472]),
    ([-2034, -7881, 2881],[-7881, -2034, 2881]),
    ([-5688, 5757, 3570, 2004],[-5688, 2004, 3570, 5757]),
    ([2072, 356, 7592, 4205, 6084],[356, 2072, 4205, 6084, 7592]) 
    ]
)
def test_mergesort(arr,expected):
    assert mergesort(arr) == expected


@pytest.mark.parametrize(
    ["arr","expected"],
    [
        ([],[]),
        ([89,90,91,91,91,100],[89,90,91,91,91,100]),
        ([76,76,76,76,76,76,76],[76,76,76,76,76,76,76]),
        ([8989899],[8989899])
    ]
)
def test_edge_cases_mergesort(arr,expected):
    assert mergesort(arr) == expected

def test_property_based_mergesort():
    for _ in range(1000):
        arr = generated_list()
        sorted_arr = mergesort(arr)
        expected = sorted(arr)
        
        assert len(sorted_arr) == len(expected)
        assert sorted_arr == expected
