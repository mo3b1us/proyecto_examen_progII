import ventana_agregar
import pandas as pd
import tkinter as tk

def modificar(producto):
    # Crear la ventana de tkinter
    ventana_modificar = tk.Tk()
    ventana_modificar.title("Modificar producto: " + producto)

    # Crear las etiquetas y los cuadros de texto para ingresar los nuevos valores
    nombre_label = tk.Label(ventana_modificar, text="Nombre:")
    nombre_label.grid(row=0, column=0)
    nombre_entry = tk.Entry(ventana_modificar)
    nombre_entry.grid(row=0, column=1)

    stock_label = tk.Label(ventana_modificar, text="Stock:")
    stock_label.grid(row=1, column=0)
    stock_entry = tk.Entry(ventana_modificar)
    stock_entry.grid(row=1, column=1)

    precio_label = tk.Label(ventana_modificar, text="Precio:")
    precio_label.grid(row=2, column=0)
    precio_entry = tk.Entry(ventana_modificar)
    precio_entry.grid(row=2, column=1)

    # Crear el botón para confirmar la modificación
    boton_modificar = tk.Button(ventana_modificar, text="Modificar", command=lambda: modificar_producto (producto,nombre_entry.get(), stock_entry.get(), precio_entry.get()))
    boton_modificar.grid(row=3, column=1)
    boton_salir = tk.Button(ventana_modificar, text="Volver", command=ventana_modificar.destroy)
    boton_salir.grid(row=5, column=1)
    
    ventana_modificar.mainloop()

def modificar_producto(producto,nombre,stock,precio):
    df = cargar_archivo()
    df.loc[df['Nombre'] == producto, 'Nombre'] = nombre
    df.loc[df['Nombre'] == nombre, 'Stock'] = stock
    df.loc[df['Nombre'] == nombre, 'Precio'] = precio
    #sobreescribimos el excel
    df.to_excel("inventario.xlsx", index=False)
