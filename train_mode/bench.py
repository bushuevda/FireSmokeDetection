from ultralytics.utils.benchmarks import benchmark


def run_benchmarks(model, data, imgsz):
  benchmark(model = model, data = data, imgsz = imgsz, format = "torchscript")
  benchmark(model = model, data = data, imgsz = imgsz, format = "onnx")
  benchmark(model = model, data = data, imgsz = imgsz, format = "openvino")
  benchmark(model = model, data = data, imgsz = imgsz, format = "tflite")
  benchmark(model = model, data = data, imgsz = imgsz, format = "paddle")
  benchmark(model = model, data = data, imgsz = imgsz, format = "mnn")
  benchmark(model = model, data = data, imgsz = imgsz, format = "ncnn")

if __name__ == "__main__":
    run_benchmarks(model="runs/detect/train40/weights/best.pt", data="data.yaml", imgsz=800)
