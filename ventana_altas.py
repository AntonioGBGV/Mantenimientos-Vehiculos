import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def altas():
    ventana_alta = Toplevel()
    ventana_alta.title("Alta Mantenimiento")
    ventana_alta.geometry("680x320")

    # Definir una fuente más grande
    fuente_grande = ("Arial", 12)

    entry_vehiculo = tk.Entry(ventana_alta, font=fuente_grande)
    entry_matricula = tk.Entry(ventana_alta, font=fuente_grande)
    entry_fecha = tk.Entry(ventana_alta, font=fuente_grande)
    entry_taller = tk.Entry(ventana_alta, font=fuente_grande)
    entry_precio = tk.Entry(ventana_alta, font=fuente_grande)
    entry_kilometros = tk.Entry(ventana_alta, font=fuente_grande)
    entry_comentarios = tk.Text(ventana_alta, height=5, width=40, font=fuente_grande)
    
    tk.Label(ventana_alta, text="Vehículo:", font=fuente_grande).grid(column=0, row=1, padx=10, pady=5, sticky=W)
    entry_vehiculo.grid(column=1, row=1, columnspan=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Matrícula:", font=fuente_grande).grid(column=0, row=3, padx=10, pady=5, sticky=W)
    tk.Label(ventana_alta, text="Kilometros:", font=fuente_grande).grid(column=2, row=3, padx=10, pady=5, sticky=W)
    entry_matricula.grid(column=1, row=3, padx=10, pady=5, sticky=EW)
    entry_kilometros.grid(column=3, row=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Fecha:", font=fuente_grande).grid(column=0, row=5, padx=10, pady=5, sticky=W)
    entry_fecha.grid(column=1, row=5, columnspan=3, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Taller:", font=fuente_grande).grid(column=0, row=7, padx=10, pady=5, sticky=W)
    tk.Label(ventana_alta, text="Precio:", font=fuente_grande).grid(column=2, row=7, padx=10, pady=5, sticky=W)
    entry_taller.grid(column=1, row=7, padx=10, pady=5, sticky=EW)
    entry_precio.grid(column=3, row=7, padx=10, pady=5, sticky=EW)

    tk.Label(ventana_alta, text="Comentarios:", font=fuente_grande).grid(column=0, row=10, padx=10, pady=5, sticky=W)
    entry_comentarios.grid(column=1, row=10, columnspan=3, rowspan=3, padx=10, pady=5, sticky=NSEW)

    def insertar_mantenimiento():
        conn = sqlite3.connect("mantenimiento.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mantenimiento(vehiculo, matricula, kilometros, fecha, taller, precio, comentarios)VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (
            entry_vehiculo.get(), entry_matricula.get(), entry_kilometros.get(), entry_fecha.get(),
            entry_taller.get(), entry_precio.get(), entry_comentarios.get("1.0", tk.END).strip()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Mantenimiento insertado correctamente")
        ventana_alta.destroy()
    
    style = ttk.Style()
    style.configure("TButtonAltas.TButton",
                font=("Arial", 14, "bold"),  # Fuente más grande para el botón
                padding=10,
                relief="solid",
                background="#d4ac0d",  # Color de fondo
                foreground="black",     # Color del texto
                width=10)               # Ancho de los botones

    boton3 = ttk.Button(ventana_alta, text="Insertar", command=insertar_mantenimiento, style="TButtonAltas.TButton")
    boton3.grid(row=13, column=2, pady=10)