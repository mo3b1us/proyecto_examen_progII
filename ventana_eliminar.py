import tkinter as tk
import pandas as pd
from utils import *


def eliminar_producto(entrada_eliminar):
    nombre_producto = entrada_eliminar.get()
    limpiar_entradas(entrada_eliminar)
    try:
        df = pd.read_excel('inventario.xlsx')
        if nombre_producto not in df['Nombre'].values:
            print(f"No se encuentra el producto: {nombre_producto}")
            return False
        else:
            df = df.loc[df["Nombre"] != nombre_producto]
            df.reset_index(inplace=True, drop=True)
            df.to_excel('inventario.xlsx', index=False)
            print(f"Se ha eliminado el producto: {nombre_producto}")
            print(df)
            return True

    except FileNotFoundError:
        print("No se encuentra el archivo 'inventario.xlsx'")
        return -1


def interfaz_eliminar():
    root = tk.Tk()
    root.title("Eliminar producto")
    root.resizable(False, False)

    ventana_eliminar = tk.LabelFrame(root, bg="burlywood1", text="Introduzca el producto que desee eliminar:", font=('Comic sans', 13))
    ventana_eliminar.grid(row=0, column=0)

    etiqueta_eliminar = tk.Label(ventana_eliminar, bg="burlywood1", text='Nombre:', font=('Comic sans', 12))
    entrada_eliminar = tk.Entry(ventana_eliminar, font=('Comic sans', 12))
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar",
                               font=('Comic sans', 12),
                               command=lambda: eliminar_producto(entrada_eliminar))
    boton_volver = tk.Button(ventana_eliminar, text="Volver",
                             font=('Comic sans', 12),
                             command=root.destroy)

    objetos = [etiqueta_eliminar, entrada_eliminar, boton_eliminar, boton_volver]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    root.mainloop()
    return


if __name__ == '__main__':
    my_df = pd.DataFrame.from_dict({"Nombre": ['manzana', 'pera', 'uva'],
                                    "Stock": [2, 7, 30],
                                    "Precio": [1.5, 1.85, 0.25]})
    my_df.to_excel('inventario.xlsx', index=False)
    print(my_df)

    interfaz_eliminar()

