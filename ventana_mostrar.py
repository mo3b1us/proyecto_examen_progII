import pandas as pd
import tkinter as tk


def mostrar_productos(root):
    df = pd.read_excel('inventario.xlsx')

    etiqueta_nombre = tk.Label(root, text="Nombre", font=("Arial", 12, "bold"), bg="lightblue", fg="red")
    etiqueta_nombre.grid(row=0, column=0)
    etiqueta_stock = tk.Label(root, text="Stock", font=("Arial", 12, "bold"), bg="lightblue", fg="red")
    etiqueta_stock.grid(row=0, column=1)
    etiqueta_precio = tk.Label(root, text="Precio", font=("Arial", 12, "bold"), bg="lightblue", fg="red")
    etiqueta_precio.grid(row=0, column=2)
    for i in range(len(df)):
        tk.Label(root, text=df.Nombre[i]).grid(row=i+1, column=0)
        tk.Label(root, text=df.Stock[i]).grid(row=i+1, column=1)
        tk.Label(root, text=df.Precio[i]).grid(row=i+1, column=2)
    root.mainloop()
    return


def interfaz_mostrar():
    root = tk.Tk()
    root.title("Inventario")
    #root.geometry("200x200")

    mostrar_productos(root)

    root.mainloop()
    return


if __name__ == '__main__':
    interfaz_mostrar()
