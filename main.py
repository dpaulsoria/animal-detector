import tkinter as tk
from tkinter import ttk
from DirectoryHandle import get_folder, process_images
from ReportGenerator import generate_report, log

width = 550
height = 700

output_path = None
current_path = None

mark_images = False

show_options = False

models_list = [
    "AnimalDetector-v1e",
    "Yolo-v8l",
    "Yolo-v8m",
    "Yolo-v8n",
    "Yolo-v8s",
    "Yolo-v8x"
]

selected_model = models_list[0]

def buscar_dataset():
    global current_path
    current_path = get_folder()
    label_dataset_path.config(text=f"Path: {current_path}")

def select_output():
    global output_path
    output_path = get_folder()
    label_output_path.config(text=f"Path: {output_path}")
    
def init():
    global mark_images
    if output_path is None:
        label_error.config(text="No olvide seleccionar un directorio de SALIDA para analizar!")
        return
    elif current_path is None:
        label_error.config(text="No olvide seleccionar un directorio para analizar!")
        return
    try:
        # selected_model = combobox.get()
        progress['value'] = 0
        report = process_images((ventana, progress), (current_path, output_path), selected_model, mark_images)
        generate_report(ventana, report)
        log((current_path, output_path), report, "Éxito", "Procesamiento completado sin errores.")
    except Exception as e:
        log((current_path, output_path), [0, 0, 0, 0], "Error", str(e))
        label_error.config(text=f"Error: {e}")
        return

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Animal Detector")
ventana.geometry(f"{width}x{height}")

# Etiquetas y botones
label_intro = tk.Label(ventana, text="Bienvenido al Detector de Animales", font=("Helvetica", 16, "bold"))
label_intro.pack(pady=20)

# Directorio de Salida
frame_output = tk.Frame(ventana)
frame_output.pack(fill="x", padx=20, pady=(0, 10))
label_output = tk.Label(frame_output, text="Directorio de Salida:")
label_output.pack(side="left")
button_output = tk.Button(frame_output, text="Buscar", command=select_output)
button_output.pack(side="left", padx=(5, 0))
label_output_path = tk.Label(ventana, text="Path:")
label_output_path.pack(fill="x", padx=20, pady=(0, 20))

# Directorio de Imágenes
frame_dataset = tk.Frame(ventana)
frame_dataset.pack(fill="x", padx=20, pady=(0, 10))
label_dataset = tk.Label(frame_dataset, text="Directorio de Imágenes:")
label_dataset.pack(side="left")
button_dataset = tk.Button(frame_dataset, text="Buscar", command=buscar_dataset)
button_dataset.pack(side="left", padx=(5, 0))
label_dataset_path = tk.Label(ventana, text="Path:")
label_dataset_path.pack(fill="x", padx=20, pady=(0, 20))

# # Checkbox para marcar las imágenes
# check_mark = tk.Checkbutton(ventana, text="Marcar recuadros en Imágenes", variable=mark_images)
# check_mark.pack()

# Combobox para elegir el modelo
# combobox = ttk.Combobox(ventana, values=models_list, state="readonly")
# combobox.set(models_list[0])
# combobox.pack()
# combobox.config(state="hidden" if not show_options else "readonly")

# Barra de progreso
progress_label = tk.Label(ventana, text="Progreso actual...")
progress_label.pack()
progress = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
progress.pack(padx=10, pady=10)

# Botón de Procesar
button_process = tk.Button(ventana, text="Procesar", command=init, bg="green", fg="white")
button_process.pack(pady=20)


# Etiqueta de Error
label_error = tk.Label(ventana, text="", fg="red")
label_error.pack()

# Bucle principal de la aplicación
ventana.mainloop()
