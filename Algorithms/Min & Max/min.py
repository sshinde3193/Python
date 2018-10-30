def min_element(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]

    return min
