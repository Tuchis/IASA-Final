from PIL import Image, ImageDraw
import json
import os
import matplotlib.pyplot as plt
import cv2
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'cyan']

data_dir = './IASA_Champ_Final/app_data'
app_name = 'Setapp'
screen_id = '1707127584'

element_path = os.path.join(data_dir, app_name, screen_id)
for file in os.listdir(element_path):
    if file.endswith(".json"):
        data_path = os.path.join(element_path, file)
    if file.endswith(".png") or file.endswith(".jpg"):
        image_path = os.path.join(element_path, file)
        
with open(data_path, 'r') as f:
    data = json.load(f)

image = Image.open(image_path)
draw = ImageDraw.Draw(image)

def draw_boxes(draw, item):
    bbox = item.get('visible_bbox')
    if bbox is not None:
        x, y, width, height = bbox
        box = [x, y, x + width, y + height]
        color = colors[hash(item.get('role')) % len(colors)]
        draw.rectangle(box, outline=color)   
    children = item.get('children', [])
    for child in children:
        draw_boxes(draw, child)

draw_boxes(draw, data)

output_image_path = 'annotated_image.png'
image.save(output_image_path)
cv2.imshow('image', cv2.imread(output_image_path))
cv2.waitKey(0)
