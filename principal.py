import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import csv

from ventana_altas import *
from mostrar_resultados import *

# Función para conectar con SQLite y crear la tabla si no existe
def conectar_db():
    conexion = sqlite3.connect("mantenimiento.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mantenimiento (id INTEGER PRIMARY KEY AUTOINCREMENT, vehiculo varchar(50), matricula varchar(50), fecha date, taller varchar(100), precio float, kilometros float, comentarios varchar(300))")
    conexion.commit()
    conexion.close()

# Función para generar el fichero CSV
def generar_csv():
    conn = sqlite3.connect("mantenimiento.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mantenimiento")
    mantenimientos = cursor.fetchall()
    conn.close()

    # Nombre del archivo CSV
    nombre_archivo = "mantenimientos.csv"

    # Escribir los datos en el archivo CSV
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8-sig") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir el encabezado
        escritor_csv.writerow(["ID", "Vehículo", "Matrícula", "Fecha", "Taller", "Precio", "Kilometros", "Comentarios"])
        
        # Escribir los datos
        for mantenimiento in mantenimientos:
            escritor_csv.writerow(mantenimiento)

    messagebox.showinfo("Éxito", f"Archivo {nombre_archivo} generado correctamente")

# Interfaz principal
principal = tk.Tk()
principal.title("Mantenimiento")
principal.geometry("480x500")
principal.resizable(False, False)

tk.Label(principal, text="Mantenimiento Vehículos", font=("Arial", 20)).pack(pady=10)

imagen = PhotoImage(file="mantenimiento.png").subsample(2)
imagen_label = tk.Label(principal, image=imagen)
imagen_label.pack(pady=10)

marco = ttk.Frame(principal)
marco.pack(expand=True)

style = ttk.Style()
style.configure("TButtonPrincipal.TButton",
                font=("Arial", 18, "bold"),
                padding=10,
                background="#d4ac0d",   #color borde botón
                foreground="black",     # color de texto
                relief="solid",         # tipo de botón
                width=18)               # Ancho de los botones

boton1 = ttk.Button(marco, text="Alta Mantenimiento", command=altas, style="TButtonPrincipal.TButton")
boton1.pack(pady=5)

boton2 = ttk.Button(marco, text="Generar CSV", command=generar_csv, style="TButtonPrincipal.TButton")
boton2.pack(pady=5)

# Nuevo botón para ver los mantenimientos
boton3 = ttk.Button(marco, text="Ver Mantenimientos", command=ver_mantenimientos, style="TButtonPrincipal.TButton")
boton3.pack(pady=5)

conectar_db()
principal.mainloop()