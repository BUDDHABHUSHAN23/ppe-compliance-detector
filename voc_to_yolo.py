'''
Filename: d:/BUDDHABHUSHAN/ppe-compliance-detector/voc_to_yolo.py
Path: d:/BUDDHABHUSHAN/ppe-compliance-detector
Created Date: Sunday, July 12th 2026, 12:54:39 pm
Author: BUDDHABHUSHAN23
Work : One this file for converting the annotation into YOLO model format => class_id x_center y_center width height

Copyright (c) 2026 Your Company
'''

"""
Convert PASCAL VOC XML annotations (Kaggle Hard Hat Detection dataset)
to YOLO format .txt files, and split into train/val/test.

Expected input:
  data/raw/annotations/*.xml
  data/raw/images/*.png (or .jpg)

Output:
  data/merged/images/{train,val,test}/
  data/merged/labels/{train,val,test}/
"""

"""
Convert PASCAL VOC XML annotations (Kaggle Hard Hat Detection dataset)
to YOLO format .txt files, and split into train/val/test.

Expected input:
  data/raw/annotations/*.xml
  data/raw/images/*.png (or .jpg)

Output:
  data/merged/images/{train,val,test}/
  data/merged/labels/{train,val,test}/
"""

import os
import random
import shutil
import xml.etree.ElementTree as ET

RAW_ANN_DIR = "./data/raw/annotations"
RAW_IMG_DIR = "./data/raw/images"
OUT_DIR = "./data/merged/"

# Kaggle hard-hat-detection classes: helmet, head, person
CLASSES = ["helmet", "head", "person"]
CLASS_TO_ID = {c: i for i, c in enumerate(CLASSES)}

SPLIT_RATIOS = {"train": 0.8, "val": 0.1, "test": 0.1}


def convert_box(size, box):
    dw, dh = 1.0 / size[0], 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0 * dw
    y = (box[2] + box[3]) / 2.0 * dh
    w = (box[1] - box[0]) * dw
    h = (box[3] - box[2]) * dh
    return x, y, w, h


def convert_annotation(xml_path, out_txt_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    lines = []
    for obj in root.findall("object"):
        cls = obj.find("name").text.strip().lower()
        if cls not in CLASS_TO_ID:
            continue
        cls_id = CLASS_TO_ID[cls]
        bb = obj.find("bndbox")
        b = (
            float(bb.find("xmin").text),
            float(bb.find("xmax").text),
            float(bb.find("ymin").text),
            float(bb.find("ymax").text),
        )
        x, y, bw, bh = convert_box((w, h), b)
        lines.append(f"{cls_id} {x:.6f} {y:.6f} {bw:.6f} {bh:.6f}")

    with open(out_txt_path, "w") as f:
        f.write("\n".join(lines))


def main():
    random.seed(42)
    xml_files = [f for f in os.listdir(RAW_ANN_DIR) if f.endswith(".xml")]
    random.shuffle(xml_files)

    n = len(xml_files)
    n_train = int(n * SPLIT_RATIOS["train"])
    n_val = int(n * SPLIT_RATIOS["val"])

    splits = {
        "train": xml_files[:n_train],
        "val": xml_files[n_train:n_train + n_val],
        "test": xml_files[n_train + n_val:],
    }

    for split, files in splits.items():
        img_out = os.path.join(OUT_DIR, "images", split)
        lbl_out = os.path.join(OUT_DIR, "labels", split)
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)

        for xml_file in files:
            stem = os.path.splitext(xml_file)[0]
            xml_path = os.path.join(RAW_ANN_DIR, xml_file)

            # find matching image (png or jpg)
            img_src = None
            for ext in (".png", ".jpg", ".jpeg"):
                candidate = os.path.join(RAW_IMG_DIR, stem + ext)
                if os.path.exists(candidate):
                    img_src = candidate
                    break
            if img_src is None:
                print(f"WARNING: no image found for {stem}, skipping")
                continue

            shutil.copy(img_src, os.path.join(img_out, os.path.basename(img_src)))
            convert_annotation(xml_path, os.path.join(lbl_out, stem + ".txt"))

        print(f"{split}: {len(files)} files processed")

    # write ppe.yaml
    yaml_content = f"""path: ./{OUT_DIR}
train: images/train
val: images/val
test: images/test
names:
  0: helmet
  1: head
  2: person
"""
    with open(os.path.join(OUT_DIR, "..", "ppe.yaml"), "w") as f:
        f.write(yaml_content)
    print("Wrote data/ppe.yaml")


if __name__ == "__main__":
    main()
