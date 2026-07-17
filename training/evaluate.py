from ultralytics import YOLO

def main():
    # Load the BEST weights saved during training (not the last epoch —
    # 'best.pt' is automatically the checkpoint with lowest val loss)
    model = YOLO("runs/ppe/yolov8n_ppe_v1/weights/best.pt")

    metrics = model.val(data="data/ppe.yaml")

    print("Overall mAP@0.5:", metrics.box.map50)
    print("Overall mAP@0.5:0.95:", metrics.box.map)

    # Per-class breakdown — this is what actually matters for your use case
    class_names = model.names  # {0: 'helmet', 1: 'head', 2: 'person'}
    for i, class_map in enumerate(metrics.box.maps):
        print(f"  {class_names[i]}: mAP@0.5 = {class_map:.4f}")

if __name__ == "__main__":
    main()
