import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas

def limpiar_entradas(*entradas):
    for entrada in entradas:
        entrada.delete(0, 'end')
    return


def obtener_caracteristicas(*entradas):
    return [entrada.get() for entrada in entradas]


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
    producto = {"Nombre":nombre, "Stock":stock, "Precio":precio}
    print(producto)
    df_producto = pd.DataFrame(producto, index = [0])
    return df_producto

def agregar_producto_excel(nombre,stock,precio):
    df_arch = cargar_archivo()
    df_producto = agregar_producto(nombre, stock, precio)
    df_arch = pd.concat([df_arch, df_producto])
    print(df_arch)
    df_arch.to_excel("inventario.xlsx",index=False)

def mostrar_df():
    df = cargar_archivo()
    #ventana_df = tk.Toplevel()
    #ventana_df.title("Dataframe")
    #ventana_df.geometry("600x400")
    #frame_df = ttk.Frame(ventana_df)
    #frame_df.pack(expand=True, fill='both')
    #tabla_df = ttk.Label(frame_df, text=df.to_string())
    #tabla_df.pack(expand=True, fill='both')
    ventana_df = tk.Tk()
    table = TableCanvas(ventana_df, dataframe=df)
    table.show()
    boton_cerrar = ttk.Button(ventana_df, text="Cerrar", command=ventana_df.destroy)
    boton_cerrar.pack()
    ventana_df.mainloop()

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

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    frame_accion = tk.LabelFrame(ventana_escritura)
    frame_accion.config(bg="burlywood1")
    frame_accion.grid(row=1, column=0)

    # Creación de etiquetas y cajas de texto para ingresar los datos del producto

    boton_agregar = tk.Button(frame_accion, text="Agregar", command=lambda: (agregar_producto_excel(*obtener_caracteristicas(entrada_nombre, entrada_stock, entrada_precio)),
                                                                             limpiar_entradas(entrada_nombre, entrada_stock, entrada_precio)))
    boton_mostrar = tk.Button(frame_accion, text="Mostrar", command=lambda: mostrar_df())
    boton_salir = tk.Button(frame_accion, text="Volver", command=root.destroy)
    modificar_entry = tk.Entry(frame_accion)
    modificar_entry.grid(row=5, column=0)
    boton_modificar = tk.Button(frame_accion, text="Modificar", command=lambda: modificar(modificar_entry.get()))
    boton_modificar.grid(row=5, column=1)


    botones = [boton_agregar, boton_mostrar, boton_salir]

    for idx, boton in enumerate(botones):
        boton.grid(row=0, column=idx, sticky="news", padx=20, pady=10)

    root.mainloop()
    return


interfaz_agregar()