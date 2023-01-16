import pandas as pd
import tkinter as tk

def cargar_archivo():
    # Cargar el archivo excel en el dataframe
    try:
        df_arch = pd.read_excel('inventario.xlsx')
    except FileNotFoundError:
        df_arch = pd.DataFrame(columns=['Nombre', 'Stock', 'Precio'])
        df_arch.to_excel('inventario.xlsx')
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
    
def limpiar():
    nombre_entry.delete(0, "end")
    stock_entry.delete(0, "end")
    precio_entry.delete(0, "end")

root = tk.Tk()
root.title("Agregar producto")
# root.geometry("400x300")

frame_agregar = tk.Frame(root)
frame_agregar.pack()
label_agregar_frame = tk.LabelFrame(frame_agregar, text="Introduzca el producto:")
label_agregar_frame.config(bg="burlywood1")
label_agregar_frame.grid(row=0 ,column=0)

# Creación de etiquetas y cajas de texto para ingresar los datos del producto
nombre_label = tk.Label(label_agregar_frame, text="Nombre:", bg="burlywood1")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(label_agregar_frame)
nombre_entry.grid(row=1, column=1)

stock_label = tk.Label(label_agregar_frame, text="Stock:", bg="burlywood1")
stock_label.grid(row=2, column=0)
stock_entry = tk.Entry(label_agregar_frame)
stock_entry.grid(row=2, column=1)

precio_label = tk.Label(label_agregar_frame, text="Precio:", bg="burlywood1")
precio_label.grid(row=3, column=0)
precio_entry = tk.Entry(label_agregar_frame)
precio_entry.grid(row=3, column=1)

boton_agregar = tk.Button(label_agregar_frame, text="Añadir", command=lambda: [agregar_producto_excel(nombre_entry.get(), stock_entry.get(), precio_entry.get()) ,limpiar()])
boton_agregar.grid(row=4, column=1)

boton_salir = tk.Button(label_agregar_frame, text="Volver", command=root.destroy)
boton_salir.grid(row=4, column=2)

root.mainloop()