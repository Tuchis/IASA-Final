import os
import random
from gpt4v import gpt4v_response

file_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/train"
result_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/results/gpt4_train"

prompt = "You have a photo of UI interface of an app. Describe every element of UI. Include all buttons and text fields. Do not talk about color, style etc"
max_tokens = 800

FINAL_RUN = True
RANDOM_FILES = 40

counter = 0

file_names = []

if FINAL_RUN:

    for root, dirs, files in os.walk(file_folder, topdown=False):
        for name in files:
            if name.endswith('.png') and not name.endswith('box.png'):
                file_names.append(os.path.join(root, name))

    # Get random sample of 10 files
    file_names = random.sample(file_names, RANDOM_FILES)

    for file in file_names:
        app, screenshot = file.split('/')[-3:-1]
        response = gpt4v_response(file, prompt, max_tokens)
        content = response['choices'][0]['message']['content']
        with open(os.path.join(result_folder, f"{app}_{screenshot}.extension"), 'w') as file:
            file.write(content)
    print("\n")

print(counter)