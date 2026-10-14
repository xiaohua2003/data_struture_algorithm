# [0, 10, 100, 1000]
def count_zero(arr):
    res = 0
    for num in arr:
        string_val = str(num)
        c = 0
        for char in string_val:
            if char == "0":
                c += 1
        if c % 2 != 0:
            res += 1
    return res

