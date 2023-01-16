import tkinter as tk
import pandas as pd


def esta_en_df(producto):
    try:
        df = pd.read_excel('inventario.xlsx')
        print(df)
        return producto in df['Nombre'].values
    except FileNotFoundError:
        print("No se encuentra el archivo 'inventario.xlsx'")
        return -1


def interfaz_eliminar():
    root = tk.Tk()
    root.title("Eliminar producto")
    root.resizable(False, False)

    ventana_eliminar = tk.LabelFrame(root, text="Introduzca el producto que desee eliminar:")
    ventana_eliminar.grid(row=0, column=0)

    etiqueta_resultado = tk.Label(ventana_eliminar)
    espacio_escritura = tk.Entry(ventana_eliminar)
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=lambda: print("Eliminar"))
    boton_volver = tk.Button(ventana_eliminar, text="Volver", command=root.destroy)

    objetos = [espacio_escritura, etiqueta_resultado, boton_eliminar, boton_volver]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx, sticky="news", padx=20, pady=10)

    root.mainloop()
    return


# interfaz_eliminar()
print(esta_en_df("manzana"))
