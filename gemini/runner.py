import os
import sys
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)
from gemini_call import run_gemini

file_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/test"
result_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/gemini_test"

prompt = "You have a photo of UI interface of an app. Describe every element of UI. Include all buttons and text fields. Do not talk about color, style etc"
max_tokens = 800

FINAL_RUN = True

# response = gpt4v_response('/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/test/GlueMotion/1707240051/GlueMotion-1707240052.37.png', prompt, max_tokens)

# print(response)

# content = response['choices'][0]['message']['content']

# # Save content to .txt file in result_folder
# with open(os.path.join(result_folder, "GlueMotion-1707240051.extension"), 'w') as file:
#     file.write(content)

counter = 0

if FINAL_RUN:
    for folder in os.listdir(file_folder):
        if folder.endswith('DS_Store'):
            continue
        for screenshot in os.listdir(os.path.join(file_folder, folder)):
            if not os.path.exists(os.path.join(result_folder, f"{folder}_{screenshot}.extension")):
                if screenshot.endswith('DS_Store'):
                    continue
                for file in os.listdir(os.path.join(file_folder, folder, screenshot)):
                    if file.endswith('DS_Store'):
                        continue
                    if file.endswith('.json') or file.endswith('box.png'):
                        continue
                    else:
                        print(folder, screenshot, file)
                        counter += 1
                        image = Image.load_from_file(os.path.join(file_folder, folder, screenshot, file))
                        response = run_gemini([prompt, image])
                        # content = response['choices'][0]['message']['content']
                        with open(os.path.join(result_folder, f"{folder}_{screenshot}.extension"), 'w') as file:
                            file.write(response)

        print("\n")

print(counter)