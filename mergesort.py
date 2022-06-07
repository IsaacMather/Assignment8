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
        return

    right_start = len(array_to_sort) // 2
    merge_sort(array_to_sort[:right_start])
    merge_sort(array_to_sort[right_start:])
    merge(array_to_sort, right_start)