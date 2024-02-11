from os import listdir
import os

representation_folder_path = '/home/kuzhum/IASA/IASA-Final-Vlad/results/gpt4_final'
tsv_folder_path = '/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/test'

result_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/results/gpt4_final_tsv"

CONNECTION_PROMPT = "Here is the representation of the same UI elements. It has additional information, as coordinates of the elements. You can use this information to connect the representation with the UI elements that are present at the screen and were described above."


# Check if there is a result folder, otherwise create it
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# Get representation files
representation_files = [f for f in listdir(representation_folder_path) if f.endswith('.extension')]

print(representation_files)

app_screenshots = []

# Get App name and screenshot id
for file in representation_files:
    app_name, part = file.split('_')
    screenshot_id = part.split('.')[0]
    app_screenshots.append((app_name, screenshot_id))

print(app_screenshots)

for app, screenshot in app_screenshots:
    with open(f'{representation_folder_path}/{app}_{screenshot}.extension', 'r') as f:
        content = f.readlines()
    print(app, screenshot)
    tsv_file = False
    # Get into that folder
    for file in listdir(f'{tsv_folder_path}/{app}/{screenshot}'):
        if file.endswith('.tsv'):
            tsv_file = True
            print(file)
            with open(f'{tsv_folder_path}/{app}/{screenshot}/{file}', 'r') as f:
                tsv_content = f.readlines()
    final_content = content + ((['\n\n', CONNECTION_PROMPT, '\n'] + tsv_content) if tsv_file else [])

    with open(f'{result_folder}/{app}_{screenshot}.extension', 'w') as f:
        f.writelines(final_content)