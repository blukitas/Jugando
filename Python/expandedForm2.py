# Write Number in Expanded Form - Part 2
# This is version 2 of my 'Write Number in Exanded Form' Kata.

# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
# expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
# expanded_form(0.04) # Should return '4/100'


import math

def expanded_form(n):
    salida = ''
    decimal, entero = math.modf(n)
    for i in range(0, len(str(int(entero)))):
        operacion = (entero % 10) * (10 ** i)
        if operacion > 0:
            salida = ' + ' + str(int(operacion)) + salida
        n = int(n / 10)

    for i in range(0, len(str(decimal)[2:])):
        operacion = int(decimal * 10)
        if operacion > 0:
            salida += ' + ' + str(operacion) + '/' + str(10 ** (i+1))

        decimal = (decimal * 10) - operacion
    return salida[3:]


print expanded_form(0.004)