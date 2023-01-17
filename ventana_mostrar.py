import pandas as pd
import tkinter as tk


def mostrar_productos(venta_mostrar):
    df = pd.read_excel('inventario.xlsx')

    etiqueta_nombre = tk.Label(venta_mostrar, text="Nombre", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_nombre.grid(row=0, column=0)
    etiqueta_stock = tk.Label(venta_mostrar, text="Stock", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_stock.grid(row=0, column=1)
    etiqueta_precio = tk.Label(venta_mostrar, text="Precio", font=("Arial", 12, "bold"), bg="lightblue", fg="red", width=10)
    etiqueta_precio.grid(row=0, column=2)
    for i in range(len(df)):
        tk.Label(venta_mostrar, text=df.Nombre[i], width=10).grid(row=i+1, column=0, sticky='nswe')
        tk.Label(venta_mostrar, text=df.Stock[i], width=10).grid(row=i+1, column=1, sticky='nswe')
        tk.Label(venta_mostrar, text=df.Precio[i], width=10).grid(row=i+1, column=2, sticky='nswe')
    return


def interfaz_mostrar():
    root = tk.Tk()
    root.title("Inventario")
    root.resizable(False, False)

    ventana_mostrar = tk.Frame(root)
    ventana_mostrar.pack(expand=False, fill=tk.X)

    mostrar_productos(ventana_mostrar)
    boton_volver = tk.Button(ventana_mostrar,
                             text="Volver",
                             command=root.destroy,
                             font=('Comic sans', 12),
                             fg="red4",
                             bg="white",
                             activeforeground="red4",
                             activebackground="white",
                             borderwidth=0)
    boton_volver.grid(column=1)
    root.mainloop()
    return


if __name__ == '__main__':
    interfaz_mostrar()
