import pytest
from sorts import heapsort

@pytest.mark.parametrize(
    ["arr","expected"],
    [
      ([-9149, -562, 3749, 6055, 12, -9196],[-9196, -9149, -562, 12, 3749, 6055]),
    ([-3941, 1575, -4402],[-4402, -3941, 1575]),
    ([-1728, 3472, -6949, -72, -7581, 6474],[-7581, -6949, -1728, -72, 3472, 6474]),
    ([-5495, 3500, 7518, 1867, 7226, -3554],[-5495, -3554, 1867, 3500, 7226, 7518]),
    ([-5374, -1716, -963, 8054, -8576, 1010],[-8576, -5374, -1716, -963, 1010, 8054])  
    ]
)
def test_heapsort_true(arr,expected):
    assert heapsort(arr) == expected
    
   
   
@pytest.mark.parametrize(
    ["arr","expected"],
    [
        ([443],[443]),
        ([34,76,7878,323232,121244354],[34,76,7878,323232,121244354]),
        ([77777,6666,555,444,33,22,11],[11,22,33,444,555,6666,77777]),
        ([],[])
     ]
)
def test_edge_cases_heapsort(arr,expected):
    assert heapsort(arr) == expected


def propert_based_heapsort(generated_list):
    for _ in range(1000):
        sorted_arr = heapsort(generated_list)
        expected = sorted(sorted_arr)

        assert len(sorted_arr) == len(expected)
        assert sorted_arr == expected
