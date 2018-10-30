def min_max_element(array):
    min = array[0]
    max = array[0]
    for i in range(0, len(array), 2):
        if array[i] < array[i+1]:
            if array[i] < min:
                min = array[i]
            if array[i+1] > max:
                max = array[i+1]
        else:
            if array[i] > max:
                max = array[i]
            if array[i+1] < min:
                min = array[i+1]
    return min, max
