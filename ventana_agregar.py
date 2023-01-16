import pandas as pd
import tkinter as tk
from utils import *


def cargar_archivo():
    # Cargar el archivo excel en el dataframe
    try:
        df_arch = pd.read_excel('inventario.xlsx')
    except FileNotFoundError:
        df_arch = pd.DataFrame(columns=['Nombre', 'Stock', 'Precio'])
        df_arch.to_excel('inventario.xlsx', index=False)
    return df_arch


def agregar_producto(nombre, stock, precio):
    # Función para agregar el producto al diccionario de inventario
    producto = {"Nombre": nombre, "Stock": stock, "Precio": precio}
    print(producto)
    df_producto = pd.DataFrame(producto, index=[0])
    return df_producto


def agregar_producto_excel(nombre, stock, precio):
    df_arch = cargar_archivo()
    df_producto = agregar_producto(nombre, stock, precio)
    df_arch = pd.concat([df_arch, df_producto])
    print(df_arch)
    df_arch.to_excel("inventario.xlsx", index=False)
    return


def interfaz_agregar():
    root = tk.Tk()
    root.title("Agregar producto")
    root.resizable(False, False)
    # root.geometry("400x300")

    ventana_escritura = tk.Frame(root)
    ventana_escritura.pack()

    frame_escritura = tk.LabelFrame(ventana_escritura, text="Introduzca el producto:")
    frame_escritura.config(bg="burlywood1")
    frame_escritura.grid(row=0, column=0)

    etiqueta_nombre = tk.Label(frame_escritura, text="Nombre:", bg="burlywood1")
    entrada_nombre = tk.Entry(frame_escritura)
    etiqueta_stock = tk.Label(frame_escritura, text="Stock:", bg="burlywood1")
    entrada_stock = tk.Entry(frame_escritura)
    etiqueta_precio = tk.Label(frame_escritura, text="Precio:", bg="burlywood1")
    entrada_precio = tk.Entry(frame_escritura)

    objetos = [etiqueta_nombre, entrada_nombre, etiqueta_stock, entrada_stock, etiqueta_precio, entrada_precio]
    entradas = [entrada_nombre, entrada_stock, entrada_precio]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    frame_accion = tk.LabelFrame(ventana_escritura)
    frame_accion.config(bg="burlywood1")
    frame_accion.grid(row=1, column=0)

    # Creación de etiquetas y cajas de texto para ingresar los datos del producto

    boton_agregar = tk.Button(frame_accion,
                              text="Agregar",
                              command=lambda: (agregar_producto_excel(*obtener_caracteristicas(*entradas)),
                                               limpiar_entradas(*entradas)))
    boton_salir = tk.Button(frame_accion, text="Volver", command=root.destroy)

    botones = [boton_agregar, boton_salir]

    for idx, boton in enumerate(botones):
        boton.grid(row=0, column=idx, sticky="news", padx=20, pady=10)

    root.mainloop()
    return
