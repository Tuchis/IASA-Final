# Import models
import os
from PIL import Image

# Path to the folder with the test data
test_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data_splitted/test"
result_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/results"

# Iterate through apps in folder
for folder in os.listdir(test_folder):
    # Iterate through screenshots in app folder
    for screenshot in os.listdir(os.path.join(test_folder, folder)):
        information = []
        # Iterate through files in screenshot folder
        for file in os.listdir(os.path.join(test_folder, folder, screenshot)):
            # 2 ways - .json accesibility file and image file
            if file.endswith('.json'):
                json_path = os.path.join(test_folder, folder, screenshot, file)
                with open(json_path, 'r') as file:
                    data = file.readlines()

                # Clean .json file and add to information
                
            else:
                image_path = os.path.join(test_folder, folder, screenshot, file)
                image = Image.open(image_path)

                # Get general information about the screenshot and add to information

                # Get question answers and add to information

                # Get text of screenshot and add to information

                # Recogntion?
        
        # Save information to .extension file
        with open(os.path.join(result_folder, f"{folder}_{screenshot}.extension"), 'w') as file:
            file.write('\n'.join(information))
