import pandas as pd
import tkinter as tk
from ventana_agregar import *
from ventana_eliminar import *


def main():
    # Frame raiz
    root = tk.Tk()
    root.title("Gestion de inventario")
    root.resizable(False, False)

    # Frame que contiene los botones con las posibles opciones
    menu = tk.Frame(root)
    menu.grid(row=0, column=0)

    # Lista con los nombres de las acciones que se realizaran al pulsar cada boton
    acciones = ["Agregar producto", "Eliminar producto", "Modificar producto", "Mostrar todos"]

    # Creamos los botones
    boton_agregar = tk.Button(menu, text=acciones[0], command=interfaz_agregar, bg="gainsboro")
    boton_eliminar = tk.Button(menu, text=acciones[1], command=interfaz_eliminar, bg="gainsboro")
    boton_modificar = tk.Button(menu, text=acciones[2], command=lambda: print(acciones[2]), bg="gainsboro")
    boton_mostrar = tk.Button(menu, text=acciones[3], command=lambda: print(acciones[3]), bg="gainsboro")

    # Lista con los objetos boton
    opciones = [boton_agregar, boton_eliminar, boton_modificar, boton_mostrar]

    # Colocamos los botones usando un bucle
    for idx, boton_opcion in enumerate(opciones):
        boton_opcion.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    # Boton para salir
    boton_salir = tk.Button(menu, text="Salir", command=root.destroy, bg="gainsboro")
    boton_salir.grid(row=3, columnspan=2, sticky="news", padx=20, pady=10)

    root.mainloop()
    return


if __name__ == '__main__':
    my_df = pd.DataFrame.from_dict({"Nombre": ['manzana', 'pera', 'uva'],
                                    "Stock": [2, 7, 30],
                                    "Precio": [1.5, 1.85, 0.25]})
    my_df.to_excel('inventario.xlsx', index=False)
    print(my_df)
    main()
