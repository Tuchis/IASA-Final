import json
import cv2
import numpy as np
import ultralytics


model = ultralytics.YOLO('best.pt')
cat_names = model.names

def fix_json(node, image):
    """
    :param node: JSON of GUI
    :param image_screenshot: cv2 image of GUI
    :return: cv2 image
    """
    if node['visible_bbox'] is not None:
        x, y, w, h = node['visible_bbox']
        yolo_res = model(cv2.resize(image[y:y+h,x:x+w,::-1], (244, 244)), verbose=False)
        top5 = [cat_names[i] for i in yolo_res[0].probs.top5]
        if np.sum(image[y:y+h, x:x+w] - image[y,x]) != 0 and node['role'] in top5:
            # image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            node['visible_bbox'] = 'null'

    if node['children']:
        for child in node['children']:
            fix_json(child, image)
    
    return None

def filter_json(json_path: str, image_path: str):
    with open(json_path) as f:
        data = json.load(f)

    json_name = json_path.split('.')[:-1]
    json_name = '.'.join(json_name)

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fix_json(data, image)
    with open(f"{json_name}_filtered.json", 'w') as f:
        data = json.dump(data, f, indent=4)
    return data, image

if __name__ == "__main__":
    json_path = "./IASA_Champ_Final/app_data/Almighty/1707228245/com.onmyway133.Almighty-setapp.json"
    image_path = "./IASA_Champ_Final/app_data/Almighty/1707228245/Almighty-1707228246.51.png"
    filter_json(json_path, image_path)
