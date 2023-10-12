from DS_day_2 import *


def test_merge_lists():
    l = [1, 3, 5, 7, 9]
    r = [2, 4, 6, 8, 10]
    assert merge_lists(l, r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    l = [2, 3, 4, 5]
    r = [1, 6, 7, 8, 9, 10]
    assert merge_lists(l, r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def test_merge_sort():
    
    l = [1, 3, 5, 7, 9]
    r = [2, 4, 6, 8, 10]
    assert merge_sort(l + r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    l = [2, 3, 4, 5]
    r = [1, 6, 7, 8, 3, 9, 10]
    assert merge_sort(l + r) == [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

def test_radix_sort():
    l = [1, 3, 5, 7, 9]
    assert radix_sort(l) == [1, 3, 5, 7, 9]

    l = [2, 3, 1,  4, 5]
    assert radix_sort(l) == [1, 2, 3, 4, 5]

    l = [2, 3, 1,  4, 5, 10, 9, 8, 7, 6]
    assert radix_sort(l) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_bucket_sort():
    l = [1, 3, 5, 7, 9]
    assert bucket_sort(l) == [1, 3, 5, 7, 9]

    l = [2, 3, 1,  4, 5]
    assert bucket_sort(l) == [1, 2, 3, 4, 5]

    l = [2, 3, 1,  4, 5, 10, 9, 8, 7, 6]
    assert bucket_sort(l) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_counting_sort():
    l = [1, 3, 5, 7, 9]
    assert counting_sort(l) == [1, 3, 5, 7, 9]

    l = [2, 3, 1,  4, 5]
    assert counting_sort(l) == [1, 2, 3, 4, 5]

    l = [2, 3, 1,  4, 5, 10, 9, 8, 7, 6]
    assert counting_sort(l) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    


def run_all_tests():
    print("Running tests - Part 2")
    test_merge_lists()
    print("merge_lists tests passed.")

    test_merge_sort()
    print("merge_sort tests passed.")

    print("Part 2 - All tests passed.")

    print("Running tests - Part 3")

    test_radix_sort()
    print("radix_sort tests passed.")

    test_bucket_sort()
    print("bucket_sort tests passed.")

    test_counting_sort()
    print("counting_sort tests passed.")

    print("Part 3 - All tests passed.")

    print("All tests passed.")


run_all_tests()