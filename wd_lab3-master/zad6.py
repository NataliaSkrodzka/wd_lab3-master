def ciag_iloczyn(a=1, b=4, ile=10):
    c = 1
    for i in range(ile+1):
        i -= 1
        c = a * b ** i
    return c


print(ciag_iloczyn(1, 2, 4))
