def max_element(array):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    return max
