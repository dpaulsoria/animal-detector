import tkinter as tk
from tkinter import filedialog
import os
import cv2
import time
import unicodedata
from ImageClassifier import classify
from PIL import Image
import io
import numpy as np
# from ReportGenerator import create_progress_bar, update_progress_bar, close_progress_bar

extensions = ('.png', '.jpg', '.jpeg')

def pil_to_cv2(img):
    try:
        image_np = np.array(img)
        return image_np
    except Exception as e:
        print(f"Error al convertir imagen de PIL a CV2: {e}")
        return None

def load_image(encoded_path):
    try:
        path = encoded_path.decode('utf-8')
        
        with open(path, 'rb') as img_file:
            img = Image.open(io.BytesIO(img_file.read()))
        
        return img
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None


def get_folder():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    return folder


def normalize_filename(filename):
    return unicodedata.normalize('NFKD', filename).encode('utf-8', 'ignore').decode('utf-8')


def update_progress_bar(num_processed, files, progress, ventana):
    progress_percent = (num_processed / len(files)) * 100
    progress_percent = round(progress_percent, 2)
    # update_progress_bar(progress_bar, progress_percent)
    progress['value'] = progress_percent
    ventana.update_idletasks()

def process_images(gui, folders, selected_model, mark):
    ventana, progress = gui
    directory, output = folders
    # progress_bar = create_progress_bar()
    
    start_time = time.time()
    num_processed = 0
    num_with_animals = 0
    num_without_animals = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                image_path = os.path.join(root, file)
                image_path = os.path.normpath(image_path)
                img = pil_to_cv2(load_image(image_path.encode('utf-8')))
                print(f"Image to process: {image_path}")
                new_img, num_boxes = classify(img, selected_model, mark)
                flag = num_boxes > 0
                if (flag):
                    num_with_animals += 1
                else:
                    num_without_animals += 1
                # No utilizamos la nueva imagen, porque classify nos devuelve
                # una imagen 640x640 y lo que queremos es que se redistribuyan
                # las imagenes en el directorio actual
                collect_images(output, flag, image_path)
                # print(f"Processed: {image_path}")
                print(f"Number of boxes: {num_boxes}")
                num_processed += 1
                update_progress_bar(num_processed, files, progress, ventana)
                
    end_time = time.time()
    
    duration = end_time - start_time
    # close_progress_bar(progress_bar)
    return (num_processed, num_with_animals, num_without_animals, duration)


def collect_images(output, flag, current_directory):
    subfolder = 'Animals' if flag else "No-Animals"
    output_path = os.path.join(output, subfolder)
    os.makedirs(output_path, exist_ok=True)  # Crea el directorio si no existe
    move_images(current_directory, output_path)


def move_images(current_dir, new_dir):
    try:
        os.rename(
            current_dir, 
            os.path.join(new_dir, os.path.basename(current_dir))
        )
        print(f"Moved {current_dir} to {new_dir}")
    except Exception as e:
        print(f"Error moving image: {e}")