# Create a function that differentiates a polynomial for a given value of x.

# Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

# Assumptions:
# There will be a coefficient near each x, unless the coefficient equals 1 or -1.
# There will be an exponent near each x, unless the exponent equals 0 or 1.
# All exponents will be greater or equal to zero
# Examples:
# differenatiate("12x+2", 3)      ==>   returns 12
# differenatiate("x^2+3x+2", 3)   ==>   returns 9
# https://www.codewars.com/kata/566584e3309db1b17d000027


def differenatiate(s, p):
    s_eval = ''
    for i in range(0, len(s)):
        if s[i] == 'x':
            if i != 0:
                s_eval += '*'
            s_eval += str(p)
        else:
            s_eval += s[i]
    print(s_eval)
    return eval(s_eval)


print(differenatiate("12x+2", 3))
print(differenatiate("x^2+3x+2", 3))