# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!


def expanded_form(n):
    salida = ''
    for i in range(0, len(str(n))):
        operacion = (n % 10) * (10 ** i)
        if operacion > 0:
            salida = ' + ' + str(operacion) + salida
        n = int(n / 10)
    return salida[3:]


print( expanded_form(70304))