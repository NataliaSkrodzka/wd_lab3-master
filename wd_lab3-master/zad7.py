from math import sqrt

liczba = input('Podaj liczbe a podam ci jej pierwiastek:')
try:
    print(sqrt(float(liczba)))
except ValueError:
    print('Pierwiastek z liczby ujemnej nieistnieje')



