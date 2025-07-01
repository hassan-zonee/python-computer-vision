from ultralytics import YOLO

model = YOLO("yolov8n.pt")

predict = model.predict(source="https://ultralytics.com/images/bus.jpg", show=True)
predict.show()