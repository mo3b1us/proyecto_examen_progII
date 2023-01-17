import pandas as pd
import tkinter as tk
from utils import *


def agregar_producto(entradas):
    nombre, stock, precio = obtener_caracteristicas(entradas)
    limpiar_entradas(entradas)
    producto = [{"Nombre": nombre, "Stock": stock, "Precio": precio}]
    df_producto = pd.DataFrame.from_dict(producto)
    try:
        df = pd.read_excel('inventario.xlsx')
    except FileNotFoundError:
        print("No se encontro el fichero 'inventario.xlsx'")
        df = pd.DataFrame(columns=['Nombre', 'Stock', 'Precio'])
    except Exception:
        print("Ha ocurrido un error inesperado")
        df = pd.DataFrame(columns=['Nombre', 'Stock', 'Precio'])
    df = pd.concat([df, df_producto], ignore_index=True)
    print(df)
    df.to_excel("inventario.xlsx", index=False)
    return


def interfaz_agregar():
    root1 = tk.Tk()
    root1.title("Agregar producto")
    root1.resizable(False, False)
    # root.geometry("400x300")

    ventana_escritura = tk.Frame(root1)
    ventana_escritura.pack()

    frame_escritura = tk.LabelFrame(ventana_escritura, text="Introduzca el producto:", font=('Comic sans', 15))
    frame_escritura.config(bg="burlywood1")
    frame_escritura.grid(row=0, column=0, sticky="nswe")

    etiqueta_nombre = tk.Label(frame_escritura, text="Nombre:", bg="burlywood1", font=('Comic sans', 12))
    entrada_nombre = tk.Entry(frame_escritura, font=('Comic sans', 12))
    etiqueta_stock = tk.Label(frame_escritura, text="Stock:", bg="burlywood1", font=('Comic sans', 12))
    entrada_stock = tk.Entry(frame_escritura, font=('Comic sans', 12))
    etiqueta_precio = tk.Label(frame_escritura, text="Precio:", bg="burlywood1", font=('Comic sans', 12))
    entrada_precio = tk.Entry(frame_escritura, font=('Comic sans', 12))

    objetos = [etiqueta_nombre, entrada_nombre, etiqueta_stock, entrada_stock, etiqueta_precio, entrada_precio]
    entradas = [entrada_nombre, entrada_stock, entrada_precio]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx // 2, column=idx % 2, sticky="nsew", padx=20, pady=20)

    frame_accion = tk.Frame(ventana_escritura)
    frame_accion.config(bg="burlywood1")
    frame_accion.grid(row=1, column=0, sticky='nsew')

    boton_agregar = tk.Button(frame_accion,
                              text="Agregar",
                              command=lambda: agregar_producto(entradas),
                              font=('Comic sans', 20),
                              fg="red4",
                              bg="white",
                              activeforeground="red4",
                              activebackground="white",
                              borderwidth=0)

    boton_volver = tk.Button(frame_accion,
                              text="Volver",
                              command=root1.destroy,
                              font=('Comic sans', 20),
                              fg="red4",
                              bg="white",
                              activeforeground="red4",
                              activebackground="white",
                              borderwidth=0)

    botones = [boton_agregar, boton_volver]

    for idx, boton in enumerate(botones):
        boton.grid(row=0, column=idx, sticky="nsew", padx=40, pady=10)

    root1.mainloop()
    return

if __name__ == '__main__':
    my_df = pd.DataFrame.from_dict({"Nombre": ['manzana', 'pera', 'uva'],
                                    "Stock": [2, 7, 30],
                                    "Precio": [1.5, 1.85, 0.25]})
    my_df.to_excel('inventario.xlsx', index=False)
    print(my_df)

    interfaz_agregar()




