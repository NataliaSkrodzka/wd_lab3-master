# a, b, c, gdzie c jest najdłuższym bokiem, jest prostokątny jeśli c²=a²+b²
def czy_prostokatny(a, b, c):
    if a >= b and a >= c:
        najdluzszy = a
        pozostaly1 = b
        pozostaly2 = c
    elif b >= a and b >= c:
        najdluzszy = b
        pozostaly1 = a
        pozostaly2 = c
    else:
        najdluzszy = c
        pozostaly1 = a
        pozostaly2 = b
    if najdluzszy**2 == pozostaly1**2 + pozostaly2**2:
        print('trojkat jest prostokatny')
        return 1
    else:
        print('trojkat nie jest prostokatny')
        return 0


print(czy_prostokatny(2, 5, 2.5))

