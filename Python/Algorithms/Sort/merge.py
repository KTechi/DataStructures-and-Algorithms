def merge(array):
    buf = [0 for _ in range(len(array))]
    func_divide(array, buf, 0, len(array)-1)

def func_divide(array, buf, l, r):
    if r <= l:
        return
    m = (l + r) // 2
    func_divide(array, buf, l, m)
    func_divide(array, buf, m+1, r)
    func_merge(array, buf, l, m, r)

def func_merge(array, buf, L_beg, L_end, R_end):
    l = L_beg
    r = L_end + 1
    i = l
    while l <= L_end and r <= R_end:
        if array[l] <= array[r]:
            buf[i] = array[l]
            l += 1
        else:
            buf[i] = array[r]
            r += 1
        i += 1
    while l <= L_end:
        buf[i] = array[l]
        i += 1
        l += 1
    while r <= R_end:
        buf[i] = array[r]
        i += 1
        r += 1
    for i in range(L_beg, R_end+1):
        array[i] = buf[i]
