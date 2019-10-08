# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
#   'abba' & 'baab' == true
#   'abba' & 'bbaa' == true
#   'abba' & 'abbba' == false
#   'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list.
#   You will be given two inputs a word and an array with words.
#   You should return an array of all the anagrams or an empty array if there are none.
#   For example:
#       anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#       anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#       anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# https://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(palabra, lista):
    salida = []
    my_dict = dict((key, palabra.count(key)) for key in palabra)
    for i in [x for x in lista if len(x) == len(palabra)]:
        es_anagrama = True
        for j in range(0, len(i)):
            # es_anagrama &= (palabra.count(palabra[j]) == i.count(i[j]) and palabra.count(i[j]) > 0)
            es_anagrama &= (my_dict.get(i[j], -1) == i.count(i[j]))
        if es_anagrama:
            salida.append(i)

    return salida

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))

#Optimo
def anagrams_optimo(word, words): return [item for item in words if sorted(item)==sorted(word)]
