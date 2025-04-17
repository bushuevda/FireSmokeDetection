from ultralytics import YOLO
import cv2
import numpy as np
import os



# Список цветов для различных классов
COLORS = [
    (255, 0, 0), (0, 255, 0)
]

# Функция для детекции огня и дыма на изображении
def detect_in_image(image_path, save_dir, name_model):
    # Загрузка модели YOLOv8
    model = YOLO(name_model)
    
    # Загрузка изображения
    image = cv2.imread(image_path)
    results = model(image)[0]
    
    # Получение оригинального изображения и результатов
    image = results.orig_img
    classes_names = results.names
    classes = results.boxes.cls.cpu().numpy()
    boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)

    # Подготовка словаря для группировки результатов по классам
    grouped_objects = {}

    # Рисование рамок и группировка результатов
    for class_id, box in zip(classes, boxes):
        class_name = classes_names[int(class_id)]
        color = COLORS[int(class_id) % len(COLORS)]  # Выбор цвета для класса
        if class_name not in grouped_objects:
            grouped_objects[class_name] = []
        grouped_objects[class_name].append(box)

        # Рисование рамок на изображении
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Сохранение измененного изображения
    new_image_path = save_dir + os.path.basename(os.path.splitext(image_path)[0]) + '_yolo' + os.path.splitext(image_path)[1]
    print(os.path.splitext(image_path)[0])
    cv2.imwrite(new_image_path, image)

    print(f"Processed {image_path}:")
    print(f"Saved bounding-box image to {new_image_path}")


# Функция  детекции огня и дыма на нескольких изображениях
def multi_detect_in_image(files_dir, save_dir, name_model):
    for file in os.scandir(files_dir):
        detect_in_image(files_dir + file.name, save_dir, name_model)
        os.scandir(files_dir).close()

# Функция детекции огня и дыма на видео
def detect_in_video(input_video_path, save_dir, name_model):
    # Открытие исходного видеофайла
    capture = cv2.VideoCapture(input_video_path)
    
    # Загрузка модели YOLOv8
    model = YOLO(name_model)

    # Чтение параметров видео
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Настройка выходного файла
    output_video_path =  save_dir + os.path.basename(os.path.splitext(input_video_path)[0]) + '_yolo' + os.path.splitext(input_video_path)[1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        # Захват кадра
        ret, frame = capture.read()
        if not ret:
            break

        # Обработка кадра с помощью модели YOLO
        results = model(frame)[0]

        # Получение данных об объектах
        classes_names = results.names
        classes = results.boxes.cls.cpu().numpy()
        boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)
        # Рисование рамок и подписей на кадре
        for class_id, box, conf in zip(classes, boxes, results.boxes.conf):
            if conf>0.5:
                class_name = classes_names[int(class_id)]
                color = COLORS[int(class_id) % len(COLORS)]
                x1, y1, x2, y2 = box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Запись обработанного кадра в выходной файл
        writer.write(frame)

    # Освобождение ресурсов и закрытие окон
    capture.release()
    writer.release()



if __name__ == "__main__":
    #detect_in_image('datasets/test/000734.jpg', 'test_detect_img/', 'model10.pt')
    #multi_detect_in_image('datasets/test/', 'test_detect_img_model10/', 'model10.pt')
    detect_in_video('test_vd2.mp4', 'test_detect_video/', 'model10.pt')