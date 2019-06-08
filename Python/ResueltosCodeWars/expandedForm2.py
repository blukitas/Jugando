# Write Number in Expanded Form - Part 2
# This is version 2 of my 'Write Number in Exanded Form' Kata.

# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
# expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
# expanded_form(0.04) # Should return '4/100'


def expanded_form(n):
    salida = ''
    entero = int(n)
    decimal = str(n).split('.')[1]
    for i in range(0, len(str(entero))):
        operacion = (entero % 10) * (10 ** i)
        if operacion > 0:
            salida = ' + ' + str(int(operacion)) + salida
        entero = int(entero / 10)

    contador = 1
    for i in decimal:
        if i != '0':
            salida += ' + ' + i + '/' + str(10 ** (contador))
        contador += 1
    return salida[3:]


print(expanded_form(351.025084105))

# 1.24
# 7.304
# 1.04
# 693.23459
# 30 + 1 + 9/10 + 7/100 + 8/1000 + 6/100000 + 1/1000000 + 8/10000000
# 10 + 3 + 5/10 + 9/100 + 3/1000 + 6/10000 + 6/1000000 + 2/10000000
# 90 + 7 + 9/10 + 4/100 + 6/1000 + 1/100000 + 8/1000000 + 1/10000000
# 20 + 7 + 6/10 + 3/100 + 8/1000 + 7/10000 + 6/100000 + 5/1000000 + 9/10000000
# 80 + 5 + 9/10 + 7/100 + 6/1000 + 8/10000 + 8/100000 + 2/1000000 + 6/10000000
# 30 + 4 + 1/10 + 7/100 + 4/1000 + 3/10000 + 9/100000 + 7/1000000 + 7/10000000
# 30 + 3 + 5/10 + 2/100 + 3/1000 + 4/10000 + 5/100000 + 5/1000000 + 2/10000000
# 80 + 7 + 7/10 + 3/100 + 6/1000 + 4/10000 + 9/100000 + 5/1000000 + 8/10000000
# 40 + 4 + 3/10 + 7/100 + 4/1000 + 5/10000 + 2/100000 + 6/1000000 + 7/10000000
