# INPUT
try:
    verbo = input("Ingrese un verbo en infinitivo: ")

    if verbo != verbo.strip():
        raise ValueError("El verbo no debe tener espacios extra")

    if verbo != verbo.lower():
        raise ValueError("El verbo debe escribirse en minúsculas")

    if len(verbo) < 2 or not verbo.isalpha() or verbo[-2:] not in ("ar", "er", "ir"): # el isalpha comprueba si todos los caracteres de una cadena son letras
        raise ValueError("El verbo debe terminar en ar, er o ir//no debe ser demasiado corto// no debe estar vacío//deben ser letras")

    # PROCESS
    pronombres = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]

    terminaciones = {
        "ar": ["o", "as", "a", "amos", "áis", "an"],
        "er": ["o", "es", "e", "emos", "éis", "en"],
        "ir": ["o", "es", "e", "imos", "ís", "en"]
    }

    raiz = verbo[:-2]

    tipo_verbo = verbo[-2:]

    lista_terminaciones = terminaciones[tipo_verbo]

    # OUTPUT
    for indice, pronombre in enumerate(pronombres):
        terminacion = lista_terminaciones[indice]
        print(f"{pronombre} {raiz}{terminacion}")

except ValueError as e:
    print(e)