pip install ultralytics opencv-python
from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

image_path = "image.jpg"

results = model(image_path)

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = model.names[class_id]

        print("Object:", object_name)
        print("Confidence:", round(confidence, 2))

    output = result.plot()
    cv2.imwrite("detected_output.jpg", output)

print("Object detection completed.")
print("Output saved as detected_output.jpg")
