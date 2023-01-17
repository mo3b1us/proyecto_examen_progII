from tkinter import *
def limpiar_entradas(entradas: list):
    if entradas is not list:
        entradas = list(entradas)
    for entrada in entradas:
        entrada.delete(0, 'end')
    return


def obtener_caracteristicas(entradas: list):
    if entradas is not list:
        entradas = list(entradas)
    return [entrada.get() for entrada in entradas]
