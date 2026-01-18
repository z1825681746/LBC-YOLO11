from ultralytics import YOLO

model = YOLO("/model/LBC-YOLO11/weights/best.pt")  # load an official model

model.export(format="tflite",device=0,imgsz=320)
