import io
import sys
from DS_day_6_solutions import *


def run_simulation_and_capture_output(num_tanks, num_samples, num_simulations):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    simulation(num_tanks, num_samples, num_simulations)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_simulation():
    assert run_simulation_and_capture_output(1000, 200, 1000) == "Estimated number of tanks: 1000\n"
    assert run_simulation_and_capture_output(1000, 200, 15) == "Estimated number of tanks: 1000\n"
    assert run_simulation_and_capture_output(1000, 20, 10) == "Estimated number of tanks: 990\n"
    assert run_simulation_and_capture_output(5000, 20, 10) == "Estimated number of tanks: 5132\n"


def test_binary_heap_insert():
    bh = BinaryHeap()
    bh.insert(10)
    assert bh.max() == 10


def test_binary_heap_max():
    bh = BinaryHeap()
    bh.insert(10)
    bh.insert(20)
    bh.insert(30)
    assert bh.max() == 30


def test_binary_heap_extract_max():
    bh = BinaryHeap()
    bh.insert(10)
    bh.insert(20)
    bh.insert(30)
    assert bh.extract_max() == 30
    assert bh.max() == 20


def run_all_tests():
    print("Part 1 - Running tests...")

    test_simulation()
    print("Passed test_simulation")

    print("Part 1- Passed all tests!")

    print("Part 2 - Running tests...")

    test_binary_heap_insert()
    print("Passed test_binary_heap_insert")

    test_binary_heap_max()
    print("Passed test_binary_heap_max")

    test_binary_heap_extract_max()
    print("Passed test_binary_heap_extract_max")

    print("Passed all tests!!!")


run_all_tests()
