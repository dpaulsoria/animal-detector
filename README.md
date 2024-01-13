# Animal Detector
## Description
Este proyecto es una aplicación de escritorio desarrollada en Python 3.10.x que permite clasificar un conjunto de imágenes en dos categorías: imágenes con animales y sin animales. La clasificación se realiza mediante el uso de un modelo de Inteligencia Artificial (IA) entrenado mediante Transfer Learning, utilizando como base el modelo YoloV8.


## Caraterísticas
- Clasifica imágenes utilizando un modelo de IA basado en YoloV8.
- Proporciona un informe detallado de la duración y la cantidad de imágenes clasificadas en cada categoría.
- Interfaz de usuario amigable.
## Captura de Pantalla
![image](https://github.com/dpaulsoria/animal-detector/assets/72895299/17dde14f-ffad-4f80-8ad6-b8fa2dbdd056)
## Cómo utilizarlo
1. Verificar que el archivo "best.pt" se encuentra dentro de la carpeta "model"
Dentro del repositorio se encuentra una carpeta "model" con el archivo "best.pt" que corresponde al modelo de IA entrenado con transfer-learning.  
Este archivo es muy importante,ya con este se realiza el procesamiento.
2. Instalar las dependencias
3. Seleccionar un directorio de salida
4. Seleccionar un directorio de imágenes de animales (directorio de entrada)
5. Darle a Iniciar y esperar el reporte
# Dependencias
- Tkinter
- Opencv
- Numpy
- Ultralytics
- Matplotlib
- tqdm?

String: pip install tkinter opencv-python matplotlib ultralytics tqdm
