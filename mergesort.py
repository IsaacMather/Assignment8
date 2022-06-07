def merge(list_one, list_two):
    working = []
    list_one_pos = 0
    list_two_pos = 0

    while list_one_pos < len(list_one) and list_two_pos < len(list_two):
        if list_one[list_one_pos] <= list_two[list_two_pos]:
            working.append(list_one[list_one_pos])
            list_one_pos += 1
        else:
            working.append(list_two[list_two_pos])
            list_two_pos += 1

    while list_one_pos < len(list_one):
        working.append(list_one[list_one_pos])
        list_one_pos += 1

    while list_two_pos < len(list_two):
        working.append(list_two[list_two_pos])
        list_two_pos += 1

    return working


def merge_sort(collection_to_sort):
    collection_to_sort[:] = _merge_sort(collection_to_sort)

def _merge_sort(array_to_sort):

    if len(array_to_sort) < 2:
        return array_to_sort

    right_start = len(array_to_sort) // 2
    left_half = _merge_sort(array_to_sort[:right_start])
    right_half = _merge_sort(array_to_sort[right_start:])
    return merge(left_half, right_half)


#timing results
# /Users/isaacmather/PycharmProjects/Assignment8/venv/bin/python /Users/isaacmather/PycharmProjects/Assignment8/main.py
# Merge Sort...
# Sorting 160000 items took 1.2143199199999999 seconds
# Shell Sort...
# 80000
# 40000
# 20000
# 10000
# 5000
# 2500
# 1250
# 625
# 312
# 156
# 78
# 39
# 19
# 9
# 4
# 2
# 1
# Sorting 160000 items took 1.7938307049999997 seconds
#
# Process finished with exit code 0