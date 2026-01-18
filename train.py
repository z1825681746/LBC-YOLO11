from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO("ultralytics/cfg/models/11/yolo11_qr_0107.yaml")
    results = model.train(data="ultralytics/cfg/datasets/barqrcode.yaml",
                          resume=True,
                          epochs=300,
                          project='model',
                          patience=45,
                          name='LBC-YOLO11',
                          device=0,
                          imgsz=640,
                          workers=5,
                          batch=16,
                          amp=False,
                          cls=0.96,
                          profile = True,
                          )
