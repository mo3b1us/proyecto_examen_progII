import pandas as pd
import tkinter as tk


def mostrar_productos(root):
    df = pd.read_excel('inventario.xlsx')

    etiqueta_nombre = tk.Label(root, text="Nombre", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_nombre.grid(row=0, column=0)
    etiqueta_stock = tk.Label(root, text="Stock", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_stock.grid(row=0, column=1)
    etiqueta_precio = tk.Label(root, text="Precio", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_precio.grid(row=0, column=2)
    for i in range(len(df)):
        tk.Label(root, text=df.Nombre[i], width=10).grid(row=i+1, column=0, sticky='nswe')
        tk.Label(root, text=df.Stock[i], width=10).grid(row=i+1, column=1, sticky='nswe')
        tk.Label(root, text=df.Precio[i], width=10).grid(row=i+1, column=2, sticky='nswe')
    root.mainloop()
    return


def interfaz_mostrar():
    root = tk.Tk()
    root.title("Inventario")
    root.resizable(False, False)

    ventana_mostrar = tk.Frame(root)
    ventana_mostrar.pack(expand=False, fill=tk.X)

    mostrar_productos(ventana_mostrar)

    root.mainloop()
    return


if __name__ == '__main__':
    interfaz_mostrar()
