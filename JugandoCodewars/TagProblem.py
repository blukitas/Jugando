# -*- coding: utf-8 -*-
import sys


def problema():
    tags = [
        'love',
        'family',
        'instagood',
        'photooftheday',
        'fashion', 'girl',
        'happy',
        'beautiful',
        'happy',
        'cute', 'family',
        'tbt',
        'like4like',
        'followme',
        'picoftheday',
        'follow',
        'me', 'happy',
        'selfie',
        'summer',
        'art',
        'instadaily',
        'friends', 'happy',
        'repost',
        'nature',
        'girl', 'family',
        'fun',
        'family',
        'style',
        'smile',
        'food',
        'instalike', 'photo',
        'likeforlike',
        'family',
        'travel', 'girl',
        'fitness',
        'igers', 'happy',
        'tagsforlikes',
        'ollow4follow', 'girl',
        'nofilter',
        'life',
        'beauty', 'photo',
        'amazing',
        'instamood', 'photo',
        'instagram',
        'photography',
        'vscocam',
        'sun',
        'photo',
        'music', 'family',
        'beach',
        'followforfollow',
        'bestoftheday',
        'sky',
        'ootd',
        'sunset'
    ]
    words = ['happy', 'family', 'photo']

    print("INICIO")
    print("----------------------------------------------------------------")
    # TODO: Podria limpiar los tags, trim, lower. Acá no es necesario pero considerable.
    # Que haya tags y palabras
    if len(tags) < 1 or len(words) < 1:
        print("FIN: No hay tags o palabras")
        print("----------------------------------------------------------------")
        return 0

    # Que todas las palabras existan en los tags, por lo menos alguna vez
    found = [x for x in words if tags.count(x) >= 1]
    if len(found) != len(words):
        print("Fin: No todas las palabras se encuentran en la lista de tags")
        print("----------------------------------------------------------------")
        return 0

    # Result tiene las palabras relevantes con la posicion en el array
    print("Lista valores claves y posiciones: ")
    result = []
    pos = 0
    for i in tags:
        if words.count(i) > 0:
            result.append([i, pos])
        pos += 1
    print(result)

    print("Inicio busqueda path")
    print("----------------------------------------------------------------")
    pos = 0
    salida = []
    for i in result:
        camino = buscar_path(result, pos+1, [x for x in words if x != i[0]], [i])
        # Solo caminos válidos. Con 3 resultados.
        if camino and len(camino) == 3:
            salida += [camino]
        pos += 1
    print("Lista de resultados: ")
    for i in salida:
        print("* Resultado: %s" % (i))
        print("Camino: %s -> %s -> %s" %( i[0][0], i[1][0], i[2][0]))
        print("Distancia: %i" %(i[2][1] - i[0][1]))
    print("----------------------------------------------------------------")

    min = sys.maxsize
    item = []
    print("Fin de ejecución")
    print("----------------------------------------------------------------")
    for i in salida:
        # print(i)
        distancia = i[2][1] - i[0][1]
        if distancia < min:
            min = distancia
            item = i
    print("Distancia mínima: %i (%s)" %(min, item[0][0]+" -> "+item[1][0]+" -> "+item[2][0] ))



def buscar_path(result, pos, words, path):
    # print("Path:", path, "Words: ", words, "Pos: ", pos)
    if len(words) < 1:
        return path

    salida = [x for x in path]
    for i in range(pos+1, len(result)-1):
        if words.count(result[i][0]) > 0:
            # print("Elemento: ", result[i])
            # print("Words: ", [x for x in words if x != result[i][0]])
            # print("Result: ", result)
            # print("I + 1: ", i+1)
            # print("Salida: ", salida)
            # print("Path:", salida+[result[i]])
            return salida + (buscar_path(result, i+1, [x for x in words if x != result[i][0]], [result[i]]))
    return path

problema()
