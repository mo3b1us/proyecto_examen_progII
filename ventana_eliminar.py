import tkinter as tk
import pandas as pd


def eliminar_producto(espacio_escritura):
    producto = espacio_escritura.get()
    espacio_escritura.delete(0, 'end')
    try:
        df = pd.read_excel('inventario.xlsx')
        if producto not in df['Nombre'].values:
            print(f"No se encuentra el producto: {producto}")
            return False
        else:
            df = df.loc[df["Nombre"] != producto]
            df.to_excel('inventario.xlsx', index=False)
            print(f"Se ha eliminado el producto: {producto}")
            print(df)
            return True

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
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=lambda: eliminar_producto(espacio_escritura))
    boton_volver = tk.Button(ventana_eliminar, text="Volver", command=root.destroy)

    objetos = [espacio_escritura, etiqueta_resultado, boton_eliminar, boton_volver]

    for idx, objeto in enumerate(objetos):
        objeto.grid(row=idx, sticky="news", padx=20, pady=10)

    root.mainloop()
    return

"""
my_df = pd.DataFrame.from_dict({"Nombre": ['manzana', 'pera', 'uva'],
                                "Stock": [2, 7, 30],
                                "Precio": [1.5, 1.85, 0.25]})
my_df.to_excel('inventario.xlsx', index=False)
print(my_df)

interfaz_eliminar()
"""
