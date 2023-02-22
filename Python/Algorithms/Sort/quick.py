import statistics

def quick(array):
    func_quick(array, 0, len(array)-1)

def func_quick(array, l, r):
    if r <= l or r == -1:
        return
    if r - l == 1:
        if array[r] < array[l]:
            array[l], array[r] = array[r], array[l]
        return
    i, j = l, r
    pivot = statistics.median([array[l], array[(l+r)//2] ,array[r]])
    # pivot = median(array[l], array[(l+r)//2] ,array[r])
    while True:
        while array[i] <= pivot and i < j:
            i += 1
        while pivot <= array[j] and i < j:
            j -= 1
        if j <= i:
            break
        array[i], array[j] = array[j], array[i]
    func_quick(array, l, i-1)
    func_quick(array, i, r)

# def median(a, b, c):
#     if a < b:
#         if b < c:
#             return b
#         elif c < a:
#             return a
#         else:
#             return c
#     else:
#         if c < b:
#             return b
#         elif a < c:
#             return a
#         else:
#             return c
