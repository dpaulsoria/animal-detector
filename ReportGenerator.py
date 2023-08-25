import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from datetime import datetime
from tqdm import tqdm

# def create_progress_bar():
#     progress_bar = tqdm(total=100, desc="Progreso", unit="%", dynamic_ncols=True)
#     return progress_bar

# def update_progress_bar(progress_bar, value):
#     progress_bar.update(value - progress_bar.n)
    
# def close_progress_bar(progress_bar):
#     progress_bar.close()

def destroy_active_canvas(window):
    children = window.winfo_children()
    for widget in children:
        if isinstance(widget, tk.Canvas):
            widget.destroy()
    return False

def transform_seconds(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    return hours, minutes, seconds

def generate_report(report):
    total_images = report[0]
    images_with_animals = report[1]
    images_without_animals = report[2]
    execution_time  = report[3]

    # Crea una nueva figura para el gráfico
    plt.figure(figsize=(4, 4))
    
    labels = [f'Con Animales: {images_with_animals}', f'Sin Animales: {images_without_animals}']
    sizes = [images_with_animals, images_without_animals]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode the first slice

    # Plot pie chart
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    hours, minutes, seconds = transform_seconds(execution_time)  # Asegúrate de tener esta función definida
    plt.title(f"Total de Imágenes Analizadas: {total_images} en {hours:.0f}h{minutes:.0f}m{seconds:.0f}s")

    # Mostrar el gráfico en una ventana independiente
    plt.show()

# Guarda un .log de cada ejecucion del programa con la fecha y hora de inicio, el path de la carpeta de entrada, el path de la carpeta de salida, 
# el numero de imagenes procesadas, el numero de imagenes con animales, el numero de imagenes sin animales y el tiempo de ejecucion
# incluso de los fallidos con un estado y un mensaje de error
def log(folders, report, status, message):
    input_folder, output_folder = folders
    total_images = report[0]
    images_with_animals = report[1]
    images_without_animals = report[2]
    execution_time  = report[3]
    with open("log.txt", "a") as file:
        file.write(f"----------------------------------------\n")
        file.write(f"Fecha y Hora: {datetime.now()}\n")
        file.write(f"Path de la carpeta de entrada: {input_folder}\n")
        file.write(f"Path de la carpeta de salida: {output_folder}\n")
        file.write(f"Numero de imagenes procesadas: {total_images}\n")
        file.write(f"Numero de imagenes con animales: {images_with_animals}\n")
        file.write(f"Numero de imagenes sin animales: {images_without_animals}\n")
        file.write(f"Tiempo de ejecucion: {execution_time}\n")
        file.write(f"Estado: {status}\n")
        file.write(f"Mensaje: {message}\n")
        file.write(f"----------------------------------------\n")
        file.close()
        
        
    