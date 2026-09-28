def find_maxmin(array):
    maxmin = []
    max = None
    min = None
    for i in array:
        if max is None or max < i:
            max = i
        if min is None or min > i:
            min = i

    maxmin.append(min)
    maxmin.append(max)
    return maxmin

