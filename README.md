啊，我明白了，你是想整个 README.md 的命令部分和关键说明都 **保持格式清晰，同时加粗关键说明**，而不是分散的标题。这里我帮你整理成一段完整、可直接放 GitHub 的源码，同时命令保持独立、关键说明加粗：

````markdown
# LBC-YOLO11: Lightweight Barcode and QR Code Detection Network

This repository contains the implementation, preprocessing scripts, and datasets for **LBC-YOLO11**, a lightweight YOLO-based object detection model designed for efficient barcode and QR code detection on mobile and embedded CPU platforms.

## Dataset Download

You can download the training and test datasets from the following sources:

- [Baidu AI Studio Dataset 1](https://aistudio.baidu.com/datasetdetail/294398)  
- [Kaggle Barcode & QR Dataset](https://www.kaggle.com/datasets/jonathanimmanuel/barcode-and-qr)  
- [Baidu AI Studio Dataset 2](https://aistudio.baidu.com/dataset/detail/367299/file)

## Installation

Install the required Python dependencies:

```bash
pip install ultralytics
````

## Training, Validation, and Export

**Train the model:**

```bash
python train.py
```

**Validate the trained model:**

```bash
python val.py
```

**Export the trained model to TFLite:**

```bash
python out.py
```

**The exported `.tflite` model can be used for real-time inference on Android devices.**
**Deployment on Android:** Integrate the exported TFLite model into an Android Studio project. Use standard TFLite APIs to perform inference on CPU, GPU, or NPU. Adjust threads or input resolution for optimal performance on different devices.


