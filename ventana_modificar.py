import tkinter as tk
import pandas as pd
from utils import *


def modificar_producto(entradas):
    nombre_modificar, nuevo_nombre, nuevo_stock, nuevo_precio = obtener_caracteristicas(entradas)
    limpiar_entradas(entradas)
    try:
        df = pd.read_excel('inventario.xlsx')
        if nombre_modificar not in df['Nombre'].values:
            print(f"No se encuentra el producto: {nombre_modificar}")
            return False
        else:
            df.loc[df['Nombre'] == nombre_modificar, 'Nombre'] = nuevo_nombre
            df.loc[df['Nombre'] == nuevo_nombre, 'Stock'] = nuevo_stock
            df.loc[df['Nombre'] == nuevo_nombre, 'Precio'] = nuevo_precio
            df.to_excel('inventario.xlsx', index=False)
            print(f"Se ha modificado el producto")
            return True

    except FileNotFoundError:
        print("No se encuentra el archivo inventario.xlsx")
        return -1


def interfaz_modificar(root, menu):

    ventana_modificar = tk.Frame(root, bg="burlywood1")

    frame_modificar = tk.LabelFrame(ventana_modificar,
                                    text="Introduzca el producto a modificar y sus nuevos valores: ",
                                    font=('Comic sans', 10))
    frame_modificar.config(bg="burlywood1")
    frame_modificar.grid(row=0, column=0, sticky="nswe")

    etiqueta_modificar = tk.Label(frame_modificar, text="Nombre del producto:")
    entrada_modificar = tk.Entry(frame_modificar)
    etiqueta_nombre = tk.Label(frame_modificar, text="Nuevo nombre:")
    entrada_nombre = tk.Entry(frame_modificar)
    etiqueta_stock = tk.Label(frame_modificar, text="Nuevo stock:")
    entrada_stock = tk.Entry(frame_modificar)
    etiqueta_precio = tk.Label(frame_modificar, text="Nuevo precio:")
    entrada_precio = tk.Entry(frame_modificar)

    entradas = [entrada_modificar, entrada_nombre, entrada_stock, entrada_precio]

    frame_accion = tk.Frame(ventana_modificar)
    frame_accion.config(bg="burlywood1")
    frame_accion.grid(row=1, column=0, sticky="news")

    boton_modificar = tk.Button(frame_accion,
                                text="Modificar",
                                command=lambda: modificar_producto(entradas),
                                font=('Comic sans', 12),
                                fg="red4",
                                bg="white",
                                activeforeground="red4",
                                activebackground="white",
                                borderwidth=0)
    boton_volver = tk.Button(frame_accion,
                             text="Volver",
                             command=lambda: cambiar_frame(ventana_modificar, menu),
                             font=('Comic sans', 12),
                             fg="red4",
                             bg="white",
                             activeforeground="red4",
                             activebackground="white",
                             borderwidth=0)

    objetos = [etiqueta_modificar, entrada_modificar, etiqueta_nombre, entrada_nombre, etiqueta_stock, entrada_stock,
               etiqueta_precio, entrada_precio, boton_modificar, boton_volver]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    return ventana_modificar


if __name__ == '__main__':
    my_df = pd.DataFrame.from_dict({"Nombre": ['manzana', 'pera', 'uva'],
                                    "Stock": [2, 7, 30],
                                    "Precio": [1.5, 1.85, 0.25]})
    my_df.to_excel('inventario.xlsx', index=False)
    print(my_df)

    interfaz_modificar()