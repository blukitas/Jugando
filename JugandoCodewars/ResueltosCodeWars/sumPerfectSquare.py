# The task is simply stated. Given an integer n (3 < n < 109), find the length of the }
#   smallest list of perfect squares which add up to n. Come up with the best algorithm 
#   you can; you'll need it!
# Examples:
#   sum_of_squares(17) = 2 
#       17 = 16 + 1 (4 and 1 are perfect squares).
#   sum_of_squares(15) = 4 
#       15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
#   sum_of_squares(16) = 1 
#       16 itself is a perfect square.
# Time constraints:
# 5 easy (sample) test cases: n < 20
# 5 harder test cases: 1000 < n < 15000
# 5 maximally hard test cases: 5 * 1e8 < n < 1e9
# 15 random maximally hard test cases: 1e8 < n < 1e9
# # https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084


import math


# Encuentra la solución decreciente, pero no optima.
def sum_of_squares_1(n):
    salida = 0
    while n > 0:
        decimal, raiz = math.modf(math.sqrt(n))
        salida += 1
        n -= (raiz * raiz)
        print("Iteracion. N: %d, Raiz: %d, Decimal: %f" %(n ,raiz, decimal))
    return salida


def sum_of_squares(n):
    noriginal = n
    lsalida = []
    salida = 0
    decimal, raiz = math.modf(math.sqrt(n))
    # TODO: Improve. 4 es un número arbitrario.
    for i in range( int(raiz / 4 ), int(raiz) + 1 ):
        salida += 1
        n -= (i * i)
        while n > 0:
            decimal, raiz = math.modf(math.sqrt(n))
            salida += 1
            n -= (raiz * raiz)
            # print("Iteracion: %d, N: %d, Raiz: %d, Decimal: %f" %(i, n ,raiz, decimal))
        lsalida.append(salida)
        salida = 0
        n = noriginal
    return min(lsalida)


# Algunas pruebas:
print(sum_of_squares(15))
print(sum_of_squares(16))
print(sum_of_squares(17))
# Como lo preveo? Hago varios caminos y elijo el más pequeño
# Suma 16 + 1 + 1, debería ser: 9 + 9
print(sum_of_squares(18))
print(sum_of_squares(19))
print(sum_of_squares(29))
print(sum_of_squares(123456789123457))


#Otras soluciones:
#explained at: http://www.zrzahid.com/least-number-of-perfect-squares-that-sums-to-n/
def sum_of_squares_3(n):
    def is_sq(n): return int(n**0.5) * int(n**0.5) == n
    if is_sq(n): return 1
    while n & 3 == 0: n >>= 2
    if n & 7 == 7: return 4
    for i in range(1,int(n**0.5)):
        if is_sq(n-i*i): return 2
    return 3