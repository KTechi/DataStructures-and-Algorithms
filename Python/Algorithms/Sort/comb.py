def comb(array):
    gap = len(array)
    done = False
    while 1 < gap or not done:
        gap = int(gap/1.3)
        if gap == 0:
            gap = 1
        elif gap == 9 or gap == 10:
            gap = 11
        done = True
        for i in range(len(array) - gap):
            if array[i+gap] < array[i]:
                array[i], array[i+gap] = array[i+gap], array[i]
                done = False
