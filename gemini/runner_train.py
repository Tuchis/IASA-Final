import os
import sys
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)
from gemini_call import run_gemini
import random

file_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/train"
result_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/results/gemini_train"

prompt = "You have a photo of UI interface of an app. Describe every element of UI. Include all buttons and text fields. Do not talk about color, style etc"
max_tokens = 800

FINAL_RUN = True
RANDOM_FILES = 10

file_names = []

if FINAL_RUN:

    for root, dirs, files in os.walk(file_folder, topdown=False):
        for name in files:
            if name.endswith('.png') and not name.endswith('box.png'):
                file_names.append(os.path.join(root, name))

    # Get random sample of 10 files
    file_names = random.sample(file_names, RANDOM_FILES)

    for file in file_names:
        print(file)
        app, screenshot = file.split('/')[-3:-1]
        image = Image.load_from_file(file)
        response = run_gemini([prompt, image])
        with open(os.path.join(result_folder, f"{app}_{screenshot}.extension"), 'w') as file:
            file.write(response)
    print("\n")
