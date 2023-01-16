import pandas as pd
import tkinter as tk

productos = []

def cargar_archivo():
    # Cargar el archivo excel en el dataframe
    df_arch = pd.read_excel("inventario.xlsx")
    return df_arch

def salir():
    ventana_principal.destroy()

def alta_producto():
    frame_alta = tk.Frame(ventana_principal)
    frame_alta.pack()
    label_alta_frame = tk.LabelFrame(frame_alta, text="Introduzca el producto:")
    label_alta_frame.config(bg="burlywood1")
    label_alta_frame.grid(row=0 ,column=0)


    # Creación de etiquetas y cajas de texto para ingresar los datos del producto
    nombre_label = tk.Label(label_alta_frame, text="Nombre:", bg="burlywood1")
    nombre_label.grid(row=1, column=0)
    nombre_entry = tk.Entry(label_alta_frame)
    nombre_entry.grid(row=1, column=1)

    stock_label = tk.Label(label_alta_frame, text="Stock:", bg="burlywood1")
    stock_label.grid(row=2, column=0)
    stock_entry = tk.Entry(label_alta_frame)
    stock_entry.grid(row=2, column=1)

    precio_label = tk.Label(label_alta_frame, text="Precio:", bg="burlywood1")
    precio_label.grid(row=3, column=0)
    precio_entry = tk.Entry(label_alta_frame)
    precio_entry.grid(row=3, column=1)

    # Creación de botón para agregar el producto al inventario
    agregar_boton = tk.Button(label_alta_frame, text="Agregar", bg="gainsboro",command=lambda: agregar_producto(nombre_entry.get(), stock_entry.get(), precio_entry.get()))
    agregar_boton.grid(row=4,column=1)

def agregar_producto(nombre, stock, precio):
    # Función para agregar el producto al diccionario de inventario
    producto = {"nombre" :nombre,"stock": int(stock), "precio": float(precio)}
    productos.append(producto)
    print(productos)
    df = pd.DataFrame.from_dict(productos)
    # Guardar dataframe en un archivo excel
    df_arch = cargar_archivo()
    print(df_arch)
    df_merged = pd.concat([df_arch, df], axis=1)
    df_merged.to_excel('inventario.xlsx')
    return df_merged

ventana_principal = tk.Tk()
ventana_principal.title("Gestión de inventario")
ventana_principal.config(bg="lightblue")
# ventana_principal.geometry("400x300")

boton_salir = tk.Button(ventana_principal, text="Salir", command=salir)
boton_salir.pack()

boton_agregar = tk.Button(ventana_principal, text="Añadir", command=alta_producto)
boton_agregar.pack()

ventana_principal.mainloop()