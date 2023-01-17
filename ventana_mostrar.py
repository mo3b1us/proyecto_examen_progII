import pandas as pd
import tkinter as tk


def mostrar_productos():
    df = pd.read_excel('inventario.xlsx')
    root = tk.Toplevel()
    root.title("Inventario")
    nombre_label = tk.Label(root, text="Nombre", font=("Arial", 12, "bold"), bg="lightblue", fg="red").grid(row = 0, column = 0)
    stock_label = tk.Label(root, text="Stock", font=("Arial", 12, "bold"), bg="lightblue", fg="red").grid(row = 0, column = 1)
    precio_label = tk.Label(root, text="Precio", font=("Arial", 12, "bold"), bg="lightblue", fg="red").grid(row = 0, column = 2)

    for i in range(len(df)):
        tk.Label(root, text=df.Nombre[i]).grid(row=i+1, column=0)
        tk.Label(root, text=df.Stock[i]).grid(row=i+1, column=1)
        tk.Label(root, text=df.Precio[i]).grid(row=i+1, column=2)

    root.mainloop()
    return


def interfaz_mostrar():
    root = tk.Tk()
    root.title("Inventario")
    root.geometry("200x200")
    boton = tk.Button(root, text="Mostrar Inventario", command=mostrar_productos)
    boton.pack()
    root.mainloop()
    return


if __name__ == '__main__':
    interfaz_mostrar()
