import tkinter as tk
from tkinter import filedialog
import os
import cv2
import time

extensions = ('.png', '.jpg', '.jpeg')

def get_folder():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    return folder

def process_images(directory, output, function_to_apply):
    start_time = time.time()
    num_processed = 0
    num_with_animals = 0
    num_without_animals = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                image_path = os.path.join(root, file)
                img = cv2.imread(image_path)
                print(f"Image to process: {image_path}")
                new_img, num_boxes = function_to_apply(img)
                flag = num_boxes > 0
                if (flag):
                    num_with_animals += 1
                else:
                    num_without_animals += 1
                collect_images(file, output, new_img, flag)
                # print(f"Processed: {image_path}")
                print(f"Number of boxes: {num_boxes}")
                num_processed += 1
    end_time = time.time()
    
    duration = end_time - start_time
    return (num_processed, num_with_animals, num_without_animals, duration)
        

def collect_images(file, output, img, flag):
    subfolder = 'Animals' if flag else "No-Animals"
    output_path = os.path.join(output, subfolder)
    os.makedirs(output_path, exist_ok=True) # Crea el directorio si no existe
    new_path = os.path.join(output_path, f"processed_{file}")
    cv2.imwrite(new_path, img)
    print(f"Saved {new_path}")
