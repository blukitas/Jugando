def to_camel_case(cadena):
    salida = ''
    b = False
    for c in range(0, len(cadena)):
        n = ord(cadena[c])
        if n == ord('-') or n == ord('_'):
            b = True
            c += 1
            continue
            
        if b:
            salida += ''.join(cadena[c]).upper()
            b = False
        else:
            salida += chr(n)
        c += 1
    return salida