from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-seg.pt")
results = model.predict('../bus.jpg')

cv2.imshow("YOLOv8 Detection", results[0].plot())
cv2.waitKey(0)