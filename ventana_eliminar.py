import tkinter as tk
import pandas as pd


def esta_en_df(producto):
    try:
        df = pd.read_excel('inventario.xlsx')
        return producto in df
    except FileNotFoundError:
        print("No se encuentra el archivo 'inventario.xlsx'")
        return -1


def interfaz_eliminar():
    root = tk.Tk()
    root.title("Eliminar producto")
    root.resizable(False, False)

    ventana_eliminar = tk.LabelFrame(root, text="Introduzca el producto que desee eliminar:")
    ventana_eliminar.grid(row=0, column=0)

    etiqueta_resultado = tk.Label(ventana_eliminar, text="Producto eliminado con exito")
    espacio_escritura = tk.Entry(ventana_eliminar)
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=lambda: print("Eliminar"), bg="gainsboro")
    boton_volver = tk.Button(ventana_eliminar, text="Volver", command=root.destroy, bg="gainsboro")

    objetos = [espacio_escritura, etiqueta_resultado, boton_eliminar, boton_volver]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx, sticky="news", padx=20, pady=10)

    esta_en_df()

    root.mainloop()
    return


my_dict = [{"Nombre": "manzana", "Stock": 4, "Precio": 1.5}]
my_df = pd.DataFrame.from_dict(my_dict)
my_df.to_excel('inventario.xlsx')
interfaz_eliminar()
