from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-cls.pt")

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model(frame)

    cv2.imshow("YOLOv8 Detection", result[0].plot())

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()