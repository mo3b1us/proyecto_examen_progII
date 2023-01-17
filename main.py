import pandas as pd
import tkinter as tk
from ventana_agregar import *
from ventana_eliminar import *


def main():
    # Frame raiz
    root = tk.Tk()
    root.title("Gestión de inventario")
    root.resizable(False, False)

    foto_icono = PhotoImage(file='imagenes/icono_ventana.png')
    root.iconphoto(False, foto_icono)

    # Frame que contiene los botones con las posibles opciones
    menu = tk.Frame(root)
    menu.grid(row=0, column=0)
    menu.config(background='sea green')

    # Lista con los nombres de las acciones que se realizaran al pulsar cada boton
    acciones = ["Agregar producto", "Eliminar producto", "Modificar producto", "Mostrar productos"]

    foto_agregar = PhotoImage(file='imagenes/agregar.png')
    foto_eliminar = PhotoImage(file='imagenes/eliminar.png')
    foto_modificar = PhotoImage(file='imagenes/modificar.png')
    foto_mostrar = PhotoImage(file='imagenes/mostrar.png')

    color_botones_menu = 'pale green'
    # Creamos los botones
    boton_agregar = tk.Button(menu,
                              text=acciones[0]+"\t",
                              command=interfaz_agregar,
                              font=('Comic sans', 30),
                              fg="green",
                              bg=color_botones_menu,
                              activeforeground="green",
                              activebackground=color_botones_menu,
                              image=foto_agregar,
                              compound='left',
                              borderwidth=0,)
    boton_eliminar = tk.Button(menu,
                              text=acciones[1]+"\t",
                              command=interfaz_eliminar,
                              font=('Comic sans', 30),
                              fg="red",
                              bg=color_botones_menu,
                              activeforeground="red",
                              activebackground=color_botones_menu,
                              image=foto_eliminar,
                              compound='left',
                              borderwidth=0)
    boton_modificar = tk.Button(menu,
                              text=acciones[2]+"\t",
                              command=lambda: print(acciones[2]),
                              font=('Comic sans', 30),
                              fg="blue",
                              bg=color_botones_menu,
                              activeforeground="blue",
                              activebackground=color_botones_menu,
                              image=foto_modificar,
                              compound='left',
                              borderwidth=0)
    boton_mostrar = tk.Button(menu,
                              text=acciones[3]+"\t",
                              command=lambda: print(acciones[3]),
                              font=('Comic sans', 30),
                              fg="darkorange",
                              bg=color_botones_menu,
                              activeforeground="darkorange",
                              activebackground=color_botones_menu,
                              image=foto_mostrar,
                              compound='left',
                              borderwidth=0
                              )

    # Lista con los objetos boton
    opciones = [boton_agregar, boton_eliminar, boton_modificar, boton_mostrar]

    # Colocamos los botones usando un bucle
    for idx, boton_opcion in enumerate(opciones):
        boton_opcion.grid(row=idx // 2, column=idx % 2, sticky="news", padx=20, pady=10)

    # Boton para salir
    boton_salir = tk.Button(menu,
                              text="Salir",
                              command=lambda: print(acciones[3]),
                              font=('Comic sans', 30),
                              fg="red4",
                              bg="white",
                              activeforeground="red4",
                              activebackground="white",
                              borderwidth=0
                              )
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
