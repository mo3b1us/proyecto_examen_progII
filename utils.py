def limpiar_entradas(*entradas):
    for entrada in entradas:
        entrada.delete(0, 'end')
    return


def obtener_caracteristicas(*entradas):
    return [entrada.get() for entrada in entradas]
