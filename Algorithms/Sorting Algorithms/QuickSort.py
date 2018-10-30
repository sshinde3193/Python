def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_aux(array, start, end)

def quick_sort_aux(array, start, end):
    if start < end:
        marker = partition(array, start, end)
        quick_sort_aux(array, start, marker - 1)
        quick_sort_aux(array, marker + 1, end)

def partition(array, start, end):
    mid = (start + end) // 2
    pivot = array[mid]                              # Choosing pivot and moving it to the start
    swap(array, start, mid)
    marker = start
    for i in range(start+1, end+1):
        if array[i] < pivot:
            marker += 1
            swap(array, i, marker)
    swap(array, start, marker)
    return marker


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
