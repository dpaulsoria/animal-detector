import cv2
from ultralytics import YOLO
from PreprocessImages import resize_images
import os

model_directory = {
    "AnimalDetector-v1e":"best.pt",
    "Yolo-v8l":"yolov8l.pt",
    "Yolo-v8m":"yolov8m.pt",
    "Yolo-v8n":"yolov8n.pt",
    "Yolo-v8s":"yolov8s.pt",
    "Yolo-v8x":"yolov8x.pt"
}


def classify(image, selected_model, mark=True):
    model_path = os.path.join('.', 'model', model_directory[selected_model])
    model = YOLO(model_path)
    image = resize_images(image)
    outputs = model.predict(source=image)
    results = outputs[0].cpu().numpy()
    if (mark):
        for i, det in enumerate(results.boxes.xyxy):
            cv2.rectangle(image,
                        (int(det[0]), int(det[1])),
                        (int(det[2]), int(det[3])),
                        color=(0, 0, 255),
                        thickness=2,
                        lineType=cv2.LINE_AA
                        )
            cv2.putText(image,
                        text =f"id:{i}",
                        org=(int(det[0]), int(det[1])),
                        fontFace =cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1,
                        color=(0,0,255),
                        thickness=1,
                        lineType=cv2.LINE_AA
                    )
    # print("RESULTS BOXES", results.boxes)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), len(results.boxes)