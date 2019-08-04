##def permutations(s):
##    # print("Inicio")
##    # print("Palabra %s, len: %d" %(s, len(s)))
##    if len(s) == 0:
##        return ['|']
##    salida = []
##    for i in range(0, len(s)):
##        subs = [s[y] for y in range(0, len(s)) if y != i ]
##        # print("Subs: ")
##        # print(subs)
##        # resultado = permutations(subs)
##        # print("Resultado:")
##        # print(resultado)
##        for j in permutations(subs):
##            item = s[i] + j
##            if salida.count(item) == 0:
##                salida.append(item)
##    return [x.replace('|', '') for x in salida]


def permutations(a):
    # Buscar heap algorithm
    out = []
    for p in permute(list(a)):
        palabra = ''.join(x for x in p)
        if palabra not in out:
            out.append(palabra)

    return out

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


x = permutations('ab')
print("Fin - Resultado: ")
print(x)
x = permutations('abab')
print("Fin - Resultado: ")
print(x)
x = permutations('jay')
print("Fin - Resultado: ")
print(x)

# x = permutations('abab')
# print("Fin")
# print("Resultado: ")
# print(x)

# TODO: Mejorar performance
