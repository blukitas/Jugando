# def permutations(s):
#     print("Inicio")
#     print("Palabra %s, len: %d" %(s, len(s)))
#     salida = []
#     for i in range(0, len(s)):
#         item = s[i]
#         for j in range(0, len(s)):    
#             print("i: %d, s[i]: %s, j: %d, s[j]: %s" %(i, s[i], j, s[j]))
#             if i != j:
#                 item += ''.join(s[j])
#             print(item)
#         print(item)
#         salida.append(item)
#     return salida

def permutations(s):
    print("Inicio")
    print("Palabra %s, len: %d" %(s, len(s)))
    
    salida = []
    for i in range(0, len(s)):
        subs = [s[y] for y in range(0, len(s)) if y != i ]
        # print("Subs: ")
        # print(subs)
        #TODO: Esto es lo que falta. IR devolviendo y juntando bien
        resultado = permutations(subs)
        item = s[i]
        for i in resultado:
            item += i
        salida.append(item)
    return salida

x = permutations('abc')
print("Fin")
print("Resultado: ")
print(x)
# for i in abc
#     ''.join(permutation(bc))
# abc
# acb
# bac
# bca
# cab
# cba 
