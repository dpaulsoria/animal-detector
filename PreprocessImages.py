import cv2

def resize_images(image, width=640, height=640):
    image = cv2.resize(image, (width, height))
    return image