# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.


def highestValue(lista):
    VALUES_DICT = {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'd': 4,
                    'e': 5,
                    'f': 6,
                    'g': 7,
                    'h': 8,
                    'i': 9,
                    'j': 10,
                    'k': 11,
                    'l': 12,
                    'm': 13,
                    'n': 14,
                    'o': 15,
                    'p': 16,
                    'q': 17,
                    'r': 18,
                    's': 19,
                    't': 20,
                    'u': 21,
                    'v': 22,
                    'w': 23,
                    'x': 24,
                    'y': 25,
                    'z': 26
                    }
    lista = lista.split(' ')
    values = [sum([VALUES_DICT.get(letra, 0) for letra in palabra.lower()]) for palabra in lista]
    print([[VALUES_DICT.get(letra, 0) for letra in palabra.lower()] for palabra in lista])
    max_value = 0
    indice_max = 0
    for i in range(0, len(values)):
        if values[i] > max_value:
            max_value = values[i]
            indice_max = i
    print(values)
    return lista[indice_max]

print(highestValue("dzvcmvsx jewpfxbzps"))
print(highestValue("xnxybhczt wxryvtecv"))
print(highestValue("myjouiarxm wgsmiwvjwx"))
