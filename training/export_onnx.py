from ultralytics import YOLO

def main():
    model = YOLO("runs/ppe/yolov8n_ppe_v1/weights/best.pt")
    model.export(format="onnx", imgsz=640, dynamic=False)

if __name__ == "__main__":
    main()
