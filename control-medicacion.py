# Inicio del desarrollo de la app para control de medicación
# Este es un esquema básico de la aplicación usando Python sin frameworks adicionales

import json
from datetime import datetime, timedelta

# Archivo de almacenamiento
ARCHIVO_DATOS = "datos.json"

# Cargar datos del archivo JSON
def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"medicaciones": [], "panales": [], "controles": []}

# Guardar datos en el archivo JSON
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Función para agregar una medicación
def agregar_medicacion():
    nombre = input("Nombre de la medicación: ")
    dosis = input("Dosis: ")
    horario = input("Horario (HH:MM): ")
    duracion_dias = int(input("Duración en días: "))
    fecha_ultima_receta = input("Fecha de última receta (YYYY-MM-DD): ")

    nueva_medicacion = {
        "nombre": nombre,
        "dosis": dosis,
        "horario": horario,
        "duracion_dias": duracion_dias,
        "fecha_ultima_receta": fecha_ultima_receta
    }

    datos["medicaciones"].append(nueva_medicacion)
    guardar_datos(datos)
    print("\nMedicación agregada con éxito.\n")

# Función para generar recordatorios
def recordatorios_medicacion():
    print("\nRecordatorios de Medicación:\n")
    for med in datos["medicaciones"]:
        fecha_receta = datetime.strptime(med["fecha_ultima_receta"], "%Y-%m-%d")
        dias_restantes = (fecha_receta + timedelta(days=med["duracion_dias"]) - datetime.now()).days
        if dias_restantes <= 7:
            print(f"La medicación {med['nombre']} debe reponerse en {dias_restantes} días.")

# Función para generar reportes
def generar_reporte():
    print("\nReporte de Uso:\n")
    print("\nMedicaciones:")
    for med in datos["medicaciones"]:
        print(f"- {med['nombre']} (Dosis: {med['dosis']}, Horario: {med['horario']})")

    print("\nPañales:")
    for panal in datos["panales"]:
        print(f"- {panal['tipo']} (Uso diario: {panal['uso_diario']})")

    print("\nControles Médicos:")
    for control in datos["controles"]:
        print(f"- {control['tipo']} (Próximo: {control['fecha_proximo']})")

# Menú interactivo
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Agregar medicación")
        print("2. Ver recordatorios")
        print("3. Generar reporte")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_medicacion()
        elif opcion == "2":
            recordatorios_medicacion()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            print("\nSaliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

# Cargar datos iniciales
datos = cargar_datos()

# Iniciar la aplicación
if __name__ == "__main__":
    menu()
