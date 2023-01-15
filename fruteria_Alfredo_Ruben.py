import pandas as pd
import tkinter as tk


def main():
    # Frame raiz
    root = tk.Tk()
    
    root.title("Gestion de inventario")
    root.resizable(False, False)

    # Frame que contiene los botones con las posibles opciones
    menu = tk.Frame(root)
    menu.grid(row=0, column=0)

    opciones = ["Agregar producto", "Eliminar producto", "Modificar producto", "Mostrar todos"]

    for idx, opcion in enumerate(opciones):
        boton_opcion = tk.Button(menu, text=opciones[idx], command=lambda: print(opciones[idx]), bg="gainsboro")
        boton_opcion.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    # Frame que contiene el boton salir
    salir = tk.Frame(root)
    salir.grid(row=1, column=0)

    opcion_salir = tk.Button(salir, text="Salir", command=root.destroy, bg="gainsboro")
    opcion_salir.grid(row=0, column=0, sticky="news", padx=20, pady=10)

    root.mainloop()
    return









if __name__ == '__main__':
    main()