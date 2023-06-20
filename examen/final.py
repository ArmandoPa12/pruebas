from collections import Counter

class NodoArbolBinario:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None

def insertar_palabra(nodo, palabra):
    if nodo is None:
        return NodoArbolBinario(palabra)

    if palabra < nodo.palabra:
        nodo.izquierdo = insertar_palabra(nodo.izquierdo, palabra)
    elif palabra >= nodo.palabra:
        nodo.derecho = insertar_palabra(nodo.derecho, palabra)

    return nodo

def obtener_palabras_repetidas(nodo, contador):
    if nodo is not None:
        contador[nodo.palabra] += 1
        obtener_palabras_repetidas(nodo.izquierdo, contador)
        obtener_palabras_repetidas(nodo.derecho, contador)

def palabras_mas_repetidas(frase):
    palabras = frase.split()
    arbol = None

    for palabra in palabras:
        arbol = insertar_palabra(arbol, palabra)

    contador = Counter()
    obtener_palabras_repetidas(arbol, contador)

    palabras_repetidas = [palabra for palabra, count in contador.items() if count > 1]
    return palabras_repetidas
