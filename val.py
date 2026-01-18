from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    # model = YOLO("model/LBC-YOLO11/weights/best.pt")
    model = YOLO("model/LBC-YOLO11/weights/best_saved_model/best_float32.tflite")
    
    metrics = model.val(data="ultralytics/cfg/datasets/barqrcodetest.yaml", save_json = True, imgsz=640,plots = True,device=0,workers=6)  # no arguments needed, dataset and settings remembered




