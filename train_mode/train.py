from ultralytics import YOLO


if __name__ == '__main__':
    # Load a model
    model = YOLO("yolov8n.pt")  # build from YAML and transfer weights ||| yolov8n.pt

    # Train the model   patience=100, 
    results = model.train(data="data.yaml", epochs = 200, imgsz=900, device = 0, conf = 0.25, optimizer = "SGD")