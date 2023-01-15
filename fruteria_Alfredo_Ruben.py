import pandas as pd
import tkinter as tk


def main():
    root = tk.Tk()

    root.title("Gestion de inventario")
    root.resizable(False, False)

    menu = tk.Frame(root)
    menu.grid(row=0, column=0)
    opciones = ["Agregar producto", "Eliminar producto", "Modificar producto", "Mostrar todos"]

    opcion_agregar = tk.Button(menu, text=opciones[0], command=lambda: print(opciones[0]), bg="gainsboro")
    opcion_agregar.grid(row=0, column=0, sticky="news", padx=20, pady=10)

    opcion_eliminar = tk.Button(menu, text=opciones[1], command=lambda: print(opciones[1]), bg="gainsboro")
    opcion_eliminar.grid(row=0, column=1, sticky="news", padx=20, pady=10)

    opcion_modificar = tk.Button(menu, text=opciones[2], command=lambda: print(opciones[2]), bg="gainsboro")
    opcion_modificar.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    opcion_mostrar = tk.Button(menu, text=opciones[3], command=lambda: print(opciones[3]), bg="gainsboro")
    opcion_mostrar.grid(row=1, column=1, sticky="news", padx=20, pady=10)

    menu.mainloop()
    return









if __name__ == '__main__':
    main()