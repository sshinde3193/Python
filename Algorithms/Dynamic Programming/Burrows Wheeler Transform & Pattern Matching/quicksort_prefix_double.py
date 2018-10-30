def quick_sort(array, suffix_compare):
    start = 1
    end = len(array) - 1
    quick_sort_aux(array, start, end, suffix_compare)

def quick_sort_aux(array, start, end, suffix_compare):
    if start < end:
        marker = partition(array, start, end, suffix_compare)
        quick_sort_aux(array, start, marker - 1, suffix_compare)
        quick_sort_aux(array, marker + 1, end, suffix_compare)

def partition(array, start, end, suffix_compare):
    mid = (start + end) // 2
    pivot = array[mid]                              # Choosing pivot and moving it to the start
    swap(array, start, mid)
    marker = start
    for i in range(start+1, end+1):
        if suffix_compare(array[i], pivot):
            marker += 1
            swap(array, i, marker)
    swap(array, start, marker)
    return marker

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
