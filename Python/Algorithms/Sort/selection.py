def selection(array):
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
