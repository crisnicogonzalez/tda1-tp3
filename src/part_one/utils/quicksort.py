def quicksort(list):
    aux_quicksort(list, 0, len(list)-1)
    return list


def aux_quicksort(a_list, left, right):
    if left < right:
        pivot = a_list[left + 1]
        l, r = left, right
        while l <= r:
            while a_list[l] < pivot:
                l += 1
            while a_list[r] > pivot:
                r -= 1
            if l <= r:
                a_list[l], a_list[r] = a_list[r], a_list[l]
                l += 1
                r -= 1
        if left < r:
            aux_quicksort(a_list, left, r)
        if l < right:
            aux_quicksort(a_list, l, right)
    return a_list