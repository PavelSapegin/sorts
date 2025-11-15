import pytest
from sorts import mergesort

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

def propert_based_mergesort(generated_list):
    for _ in range(1000):
        sorted_arr = mergesort(generated_list)
        expected = sorted(generated_list)
        
        assert len(sorted_arr) == len(expected)
        assert sorted_arr == expected
