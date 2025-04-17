from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("yolov8n.pt") 
    results = model.train(data="data.yaml", epochs = 200, imgsz=800, device = 0, optimizer = "SGD")
