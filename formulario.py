import pandas as pd
import tkinter as tk

personas = []

# Función para agregar una persona a la lista
def agregar_persona():
    nombre = nombre_entry.get()
    apellidos = apellidos_entry.get()
    correo = correo_entry.get()
    dni = documento_entry.get()
    tel = tel_entry.get()
    persona = [nombre, apellidos, correo, dni, tel]
    personas.append(persona)

# Función para guardar los datos en un archivo Excel
def guardar_datos():
    df = pd.DataFrame(personas)
    nombre_archivo = nombre_archivo_entry.get()
    df.to_excel(nombre_archivo + ".xlsx")
    print(personas)

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
#ventana.geometry("500x300")

# Crear etiquetas y campos de entrada para cada dato de la persona
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1)

apellidos_label = tk.Label(ventana, text="Apellidos:")
apellidos_label.grid(row=1, column=0)
apellidos_entry = tk.Entry(ventana)
apellidos_entry.grid(row=1, column=1)

correo_label = tk.Label(ventana, text="Correo electrónico:")
correo_label.grid(row=2, column=0)
correo_entry = tk.Entry(ventana)
correo_entry.grid(row=2, column=1)

documento_label = tk.Label(ventana, text="Documento de identidad:")
documento_label.grid(row=3, column=0)
documento_entry = tk.Entry(ventana)
documento_entry.grid(row=3, column=1)

tel_label = tk.Label(ventana, text="Teléfono:")
tel_label.grid(row=4, column=0)
tel_entry = tk.Entry(ventana)
tel_entry.grid(row=4, column=1)

agregar_button = tk.Button(ventana, text="Agregar", command=agregar_persona)
agregar_button.grid(row=5, column=0)

nombre_archivo_label = tk.StringVar()
nombre_archivo_label.set("")
nombre_archivo_entry = tk.Entry(ventana, textvariable=nombre_archivo_label)
nombre_archivo_entry.grid(row=0, column=4)
guardar_button = tk.Button(ventana, text="Guardar", command=guardar_datos)
guardar_button.grid(row=1, column=4)

salir_button = tk.Button(ventana, text="Salir", command=salir)
salir_button.grid(row=5, column=1)

ventana.mainloop()