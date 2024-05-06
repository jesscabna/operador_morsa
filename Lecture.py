#una función para convertir una letra a Morse y después invocar a esa función por cada letra de la cadena a codificar.
def caracter_plano_a_morse(caracter):
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        # Si no existe, regresamos una cadena vacía
        return ""


def codificar_morse(texto_plano):
    # A mayúsculas para evitar hacer más comparaciones
    texto_plano = texto_plano.upper()
    morse = ""  # Aquí alojamos el resultado
    for caracter in texto_plano:
        # Por cada carácter, buscamos su equivalencia
        caracter_codificado = caracter_plano_a_morse(caracter)
        # Lo concatenamos al resultado, además de agregar un espacio
        morse += caracter_codificado + " "
    return morse