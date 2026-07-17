from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # loads pretrained weights (downloads automatically first time)

model.train(
    data="data/ppe.yaml",
    epochs=100,
    imgsz=640,
)
