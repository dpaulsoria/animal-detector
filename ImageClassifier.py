import cv2
from ultralytics import YOLO
from PreprocessImages import resize_images
model = YOLO('yolov8n.pt')


def classify(image):
    outputs = model.predict(source=image)
    results = outputs[0].cpu().numpy()
    # image = cv2.imread(image)
    image = resize_images(image)
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