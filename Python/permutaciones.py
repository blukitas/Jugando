# def permutations(s):
#     # print("Inicio")
#     # print("Palabra %s, len: %d" %(s, len(s)))
#     if len(s) == 0:
#         return ['|']

#     salida = []
#     for i in range(0, len(s)):
#         subs = [s[y] for y in range(0, len(s)) if y != i ]
#         # print("Subs: ")
#         # print(subs)
#         resultado = permutations(subs)
#         # print("Resultado:")
#         # print(resultado)
#         for j in permutations(subs):
#             item = s[i] + j
#             if salida.count(item) == 0:
#                 salida.append(item)
#     return [x.replace('|', '') for x in salida]

def permutations(s):
    salida = ''
    for i in range(0, len(s)):
        subs = ''.join(s[y] for y in range(0, len(s)) if y != i)
        print(subs)
        for j in permutations(subs):
            salida += s[i] + j + '.'
    return salida.split('.')
    
x = permutations('abc')
print("Fin")
print("Resultado: ")
print(x)

# x = permutations('abab')
# print("Fin")
# print("Resultado: ")
# print(x)

#TODO: Mejorar performance


