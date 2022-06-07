import random
import copy
import mergesort
import shellsort
import time



def test_merge_sort():
    LIST_SIZE = 160000

    list_one = list(range(0, LIST_SIZE))
    random.shuffle(list_one)
    list_two = copy.copy(list_one)

    print("Merge Sort...")
    start_time = time.perf_counter()
    mergesort.merge_sort(list_two)
    stop_time = time.perf_counter()
    elapsed = stop_time - start_time
    print("Sorting", LIST_SIZE, "items took", elapsed, "seconds")

    print("Shell Sort...")
    start_time = time.perf_counter()
    shellsort.shell_sort(list_one)
    stop_time = time.perf_counter()
    elapsed = stop_time - start_time
    print("Sorting", LIST_SIZE, "items took", elapsed, "seconds")
    assert list_one == list_two

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_merge_sort()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
