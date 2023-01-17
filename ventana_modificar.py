import tkinter as tk
import pandas as pd
from utils import *

def modificar_producto(*entradas):
    limpiar_entradas(*entradas)
    nombre_modificar = entrada_modificar.get()
    nuevo_nombre = entrada_nombre.get()

    try:
        df = pd.read_excel('inventario.xlsx')
        if nombre_modificar not in df['Nombre'].values:
            print(f"No se encuentra el producto: {nombre_modificar}")
            return False
        else:
            df.loc[df['Nombre'] == nombre_modificar, 'Nombre'] = nuevo_nombre
            df.loc[df['Nombre'] == nuevo_nombre, 'Stock'] = entrada_stock.get()
            df.loc[df['Nombre'] == nuevo_nombre, 'Precio'] = entrada_precio.get()
            df.to_excel('inventario.xlsx', index=False)
            print(f"Se ha modificado el producto")
            return True
    
    except FileNotFoundError:
        print("No se encuentra el archivo inventario.xlsx")
        return -1



def interfaz_modificar():
    root = tk.Tk()
    root.title("Modificar Producto")
    root.resizable(False, False)

    ventana_modificar = tk.LabelFrame(root, text="Introduzca el producto que desee modificar:")
    ventana_modificar.grid(row=0, column=0)

    etiqueta_modificar = tk.Label(ventana_modificar)
    entrada_modificar = tk.Entry(ventana_modificar)
    nombre_etiqueta = tk.Label(ventana_modificar, text= "Nuevo nombre:")
    entrada_nombre = tk.Entry(ventana_modificar)
    stock_etiqueta = tk.Label(ventana_modificar, text= "Nuevo stock:")
    entrada_stock = tk.Entry(ventana_modificar)
    precio_etiqueta = tk.Label(ventana_modificar, text= "Nuevo precio")
    entrada_precio = tk.Entry(ventana_modificar)
    boton_modificar = tk.Button(ventana_modificar, text="Modificar", command=lambda: modificar_producto(entradas))
    boton_volver = tk.Button(ventana_modificar, text="Volver", command=root.destroy)

    objetos = [entrada_modificar, etiqueta_modificar,nombre_etiqueta, entrada_nombre, stock_etiqueta, entrada_stock, precio_etiqueta, entrada_precio, boton_modificar, boton_volver]
    entradas = [entrada_modificar,entrada_nombre,entrada_stock,entrada_precio]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx, sticky="news", padx=20, pady=10)

    root.mainloop()
    return