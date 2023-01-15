import pandas as pd
import tkinter as tk

inventario = {}

def salir():
    ventana_principal.destroy()

def alta_producto():
    ventana_alta = tk.Toplevel(ventana_principal)
    ventana_alta.title("Agregar producto")

    # Creación de etiquetas y cajas de texto para ingresar los datos del producto
    nombre_label = tk.Label(ventana_alta, text="Nombre:")
    nombre_label.grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana_alta)
    nombre_entry.grid(row=0, column=1)

    stock_label = tk.Label(ventana_alta, text="Stock:")
    stock_label.grid(row=1, column=0)
    stock_entry = tk.Entry(ventana_alta)
    stock_entry.grid(row=1, column=1)

    precio_label = tk.Label(ventana_alta, text="Precio:")
    precio_label.grid(row=2, column=0)
    precio_entry = tk.Entry(ventana_alta)
    precio_entry.grid(row=2, column=1)

    # Creación de botón para agregar el producto al inventario
    agregar_boton = tk.Button(ventana_alta, text="Agregar", command=lambda: agregar_producto(nombre_entry.get(), stock_entry.get(), precio_entry.get()))
    agregar_boton.grid(row=3, column=0, columnspan=2)

def agregar_producto(nombre, stock, precio):
    # Función para agregar el producto al diccionario de inventario
    inventario[nombre] = {"stock": stock, "precio": precio}
    print(inventario)
    df = pd.DataFrame.from_dict(inventario, orient='index', columns=['Nombre', 'Stock', 'Precio'])
    # Guardar dataframe en un archivo excel
    df.to_excel('inventario.xlsx')

ventana_principal = tk.Tk()
ventana_principal.title("Gestión de inventario")
# ventana_principal.geometry("400x300")

boton_salir = tk.Button(ventana_principal, text="Salir", command=salir)
boton_salir.pack()

boton_agregar = tk.Button(ventana_principal, text="Añadir", command=alta_producto)
boton_agregar.pack()

ventana_principal.mainloop()