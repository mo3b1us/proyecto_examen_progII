from tkinter import *
def limpiar_entradas(entradas: list):
    if not isinstance(entradas, list):
        entradas = [entradas]
    for entrada in entradas:
        entrada.delete(0, 'end')
    return


def obtener_caracteristicas(entradas: list):
    if not isinstance(entradas, list):
        entradas = [entradas]
    return [entrada.get() for entrada in entradas]



