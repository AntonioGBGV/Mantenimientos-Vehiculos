import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def ver_mantenimientos():
    # Crear una nueva ventana
    ventana_mantenimientos = tk.Toplevel()
    ventana_mantenimientos.title("Listado de Mantenimientos")
    ventana_mantenimientos.geometry("1400x400")

    # Configurar el estilo del Treeview para usar una fuente más grande
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 12))  # Fuente más grande para el Treeview
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))  # Fuente más grande para los encabezados

    # Crear un Treeview para mostrar los datos en forma de tabla
    tree = ttk.Treeview(ventana_mantenimientos, columns=("ID", "Vehículo", "Matrícula", "Fecha", "Taller", "Precio", "Kilometros", "Comentarios"), show="headings", style="Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Vehículo", text="Vehículo")
    tree.heading("Matrícula", text="Matrícula")
    tree.heading("Fecha", text="Fecha")
    tree.heading("Taller", text="Taller")
    tree.heading("Precio", text="Precio")
    tree.heading("Kilometros", text="Kilometros")
    tree.heading("Comentarios", text="Comentarios")

    tree.column("ID", width=20, anchor="center")          # Ancho de 50 para ID
    tree.column("Vehículo", width=55, anchor="center")   # Ancho de 100 para Vehículo
    tree.column("Matrícula", width=45, anchor="center")  # Ancho de 100 para Matrícula
    tree.column("Fecha", width=45, anchor="center") # Ancho de 100 para Kilómetros
    tree.column("Taller", width=80, anchor="center")      # Ancho de 100 para Fecha
    tree.column("Precio", width=45, anchor="center")     # Ancho de 150 para Taller
    tree.column("Kilometros", width=45, anchor="center")      # Ancho de 80 para Precio
    tree.column("Comentarios", width=650, anchor="center")# Ancho de 200 para Comentarios
    tree.pack(fill="both", expand=True)

    # Obtener los datos de la base de datos
    conn = sqlite3.connect("mantenimiento.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mantenimiento")
    mantenimientos = cursor.fetchall()
    conn.close()

    # Insertar los datos en el Treeview
    for mantenimiento in mantenimientos:
        tree.insert("", "end", values=mantenimiento)
    
     # Función para ordenar por columna
    def ordenar_por_columna(tree, col, reverse):
        # Obtener todos los elementos del Treeview
        datos = [(tree.set(item, col), item) for item in tree.get_children("")]
        
        # Ordenar los datos
        if col == "Fecha":
            # Ordenar fechas (formato dd/mm/yyyy)
            datos.sort(key=lambda x: tuple(map(int, x[0].split("/")))[::-1], reverse=reverse)
        else:
            # Ordenar alfabéticamente o numéricamente
            datos.sort(reverse=reverse)

        # Reorganizar los elementos en el Treeview
        for index, (valor, item) in enumerate(datos):
            tree.move(item, "", index)

        # Cambiar el orden para la próxima vez
        tree.heading(col, command=lambda: ordenar_por_columna(tree, col, not reverse))

    # Configurar el evento de clic en los encabezados
    for col in ("ID", "Vehículo", "Matrícula", "Fecha", "Taller", "Precio", "Kilometros", "Comentarios"):
        tree.heading(col, command=lambda c=col: ordenar_por_columna(tree, c, False))
    
        # Función para editar un mantenimiento seleccionado
    def editar_mantenimiento():
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un mantenimiento para editar.")
            return

        # Obtener los datos del mantenimiento seleccionado
        item = tree.item(seleccionado)
        valores = item["values"]

        # Abrir la ventana de edición con los datos del mantenimiento seleccionado
        editar_ventana(valores)

    # Botón para editar un mantenimiento
    boton_editar = ttk.Button(ventana_mantenimientos, text="Editar", command=editar_mantenimiento)
    boton_editar.pack(pady=10)

def editar_ventana(valores):
    # Crear una nueva ventana para editar el mantenimiento
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Mantenimiento")
    ventana_editar.geometry("680x320")

    # Definir una fuente más grande
    fuente_grande = ("Arial", 12)

    # Crear campos de entrada con los datos del mantenimiento seleccionado
    entry_vehiculo = tk.Entry(ventana_editar, font=fuente_grande)
    entry_matricula = tk.Entry(ventana_editar, font=fuente_grande)
    entry_fecha = tk.Entry(ventana_editar, font=fuente_grande)
    entry_taller = tk.Entry(ventana_editar, font=fuente_grande)
    entry_precio = tk.Entry(ventana_editar, font=fuente_grande)
    entry_kilometros = tk.Entry(ventana_editar, font=fuente_grande)
    entry_comentarios = tk.Text(ventana_editar, height=5, width=40, font=fuente_grande)

    # Llenar los campos con los datos del mantenimiento seleccionado
    entry_vehiculo.insert(0, valores[1])
    entry_matricula.insert(0, valores[2])
    entry_kilometros.insert(0, valores[3])
    entry_fecha.insert(0, valores[4])
    entry_taller.insert(0, valores[5])
    entry_precio.insert(0, valores[6])
    entry_comentarios.insert("1.0", valores[7])

    # Posicionar los campos en la ventana
    tk.Label(ventana_editar, text="Vehículo:", font=fuente_grande).grid(column=0, row=1, padx=10, pady=5, sticky=W)
    entry_vehiculo.grid(column=1, row=1, columnspan=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_editar, text="Matrícula:", font=fuente_grande).grid(column=0, row=3, padx=10, pady=5, sticky=W)
    tk.Label(ventana_editar, text="Kilometros:", font=fuente_grande).grid(column=2, row=3, padx=10, pady=5, sticky=W)
    entry_matricula.grid(column=1, row=3, padx=10, pady=5, sticky=EW)
    entry_kilometros.grid(column=3, row=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_editar, text="Fecha:", font=fuente_grande).grid(column=0, row=5, padx=10, pady=5, sticky=W)
    entry_fecha.grid(column=1, row=5, columnspan=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_editar, text="Taller:", font=fuente_grande).grid(column=0, row=7, padx=10, pady=5, sticky=W)
    tk.Label(ventana_editar, text="Precio:", font=fuente_grande).grid(column=2, row=7, padx=10, pady=5, sticky=W)
    entry_taller.grid(column=1, row=7, padx=10, pady=5, sticky=EW)
    entry_precio.grid(column=3, row=7, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_editar, text="Comentarios:", font=fuente_grande).grid(column=0, row=10, padx=10, pady=5, sticky=W)
    entry_comentarios.grid(column=1, row=10, columnspan=3, rowspan=3, padx=10, pady=5, sticky=NSEW)

    # Función para guardar los cambios
    def guardar_cambios():
        conn = sqlite3.connect("mantenimiento.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE mantenimiento
            SET vehiculo=?, matricula=?, kilometros=?, fecha=?, taller=?, precio=?, comentarios=?
            WHERE id=?
        """, (
            entry_vehiculo.get(), entry_matricula.get(), entry_kilometros.get(), entry_fecha.get(),
            entry_taller.get(), entry_precio.get(), entry_comentarios.get("1.0", tk.END).strip(), valores[0]
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Mantenimiento actualizado correctamente")
        ventana_editar.destroy()

    # Botón para guardar los cambios
    boton_guardar = ttk.Button(ventana_editar, text="Guardar", command=guardar_cambios)
    boton_guardar.grid(row=13, column=2, pady=10)