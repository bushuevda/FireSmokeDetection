import json
import os


SMOKE = 3
FIRE = 4


def convert_coco_to_yolo(json_path, output_path):
    with open(json_path) as f:
        data = json.load(f)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]

        with open(os.path.join(output_path, f"{os.path.splitext(file_name)[0]}.txt"), 'w') as f:
            for ann in annotations:
                category_id = ann['category_id'] - 1
                bbox = ann['bbox']
                x_center = (bbox[0] + bbox[2] / 2) / width
                y_center = (bbox[1] + bbox[3] / 2) / height
                w = bbox[2] / width
                h = bbox[3] / height
                if category_id == SMOKE:
                    f.write(f"{category_id - SMOKE} {x_center} {y_center} {w} {h}\n")
                elif category_id == FIRE:
                    f.write(f"{category_id - FIRE + 1} {x_center} {y_center} {w} {h}\n")

json_path = 'dataset_fire_smoke/475_fire_train/annotations/instances_default.json'
output_path = 'lab'
convert_coco_to_yolo(json_path, output_path)