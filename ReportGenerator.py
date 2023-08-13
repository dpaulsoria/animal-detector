import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from datetime import datetime

def generate_report(ventana, total_images, images_with_animals, images_without_animals, execution_time):
    labels = ['Con Animales', 'Sin Animales']
    sizes = [images_with_animals, images_without_animals]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode the first slice

    fig = plt.figure(figsize=(10, 6))

    # Plot pie chart
    plt.subplot(1, 1, 1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title(f"Total de Imágenes Analizadas: {total_images} en {execution_time:.2f} segundos")

    # Embedding in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.margin = 10
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Display execution time as text
    time_label = tk.Label(ventana, text=f"Tiempo de Ejecución: {execution_time:.2f} segundos")
    time_label.pack()
    
    
# Guarda un .log de cada ejecucion del programa con la fecha y hora de inicio, el path de la carpeta de entrada, el path de la carpeta de salida, el numero de imagenes procesadas, el numero de imagenes con animales, el numero de imagenes sin animales y el tiempo de ejecucion
# incluso de los fallidos con un estado y un mensaje de error
def log(input_folder, output_folder, total_images, images_with_animals, images_without_animals, execution_time, status, message):
    pass
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
        
        
    