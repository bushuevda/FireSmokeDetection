from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("yolov8n.pt") 
    results = model.train(data="data.yaml", epochs = 200, imgsz=900, device = 0, conf = 0.25, optimizer = "SGD")
