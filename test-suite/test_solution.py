# Test suite of representations of the solution to the problem

import pandas as pd
import os
import json
import ast
from openai_client import OpenAI_Client

# Read train data
train_data_path = '/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final'
train_data_file = 'ui_questions_train.tsv'

# Path to the sample file (comment or delete for the final solution)
# train_data_file = 'ui_questions_train_test.tsv'

train_data = pd.read_csv(os.path.join(train_data_path, train_data_file), sep='\t')

image_representations_folder = "/home/kuzhum/IASA/IASA-Final-Vlad/results/gemini_test"

# Get screen representation ids from files in the folder
screen_representations = os.listdir(image_representations_folder)

# Get a value with regex that is between _ and .
screen_representations = [int(screen.split('_')[1].split('.')[0]) for screen in screen_representations]

# Get rows from the train data that are in the screen representations
train_data = train_data[train_data['Screen id'].isin(screen_representations)]

print(train_data.head(5))

# Image representations folder

def get_screen_representation(app_name, screen_id):
    path = os.path.join(image_representations_folder, f"{app_name}_{screen_id}.extension")
    with open(path, 'r') as file:
        return file.read()

# Init OpenAI client
openai_client = OpenAI_Client()

# Dictionary to store the questions and correct answers
questions = {}
correct_answers = {}

PROMPTS = json.load(open("data/prompts.json"))
for prompt in PROMPTS:
    questions[prompt] = 0
    correct_answers[prompt] = 0

# Iterate over the train data and get responses
for row_ind, row in train_data.iterrows():
    app_bundle, app_name, screen_id, question, answer, answer_type = row

    # Make screen_id a string
    screen_id = str(screen_id)

    # Find the representation of the screen
    screen_representation = get_screen_representation(app_name, screen_id)

    # Get the model response
    model_response = openai_client.get_model_response(
        answer_type,
        question, 
        screen_representation
    )

    model_response = str(model_response) 

    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print(f"Model response: {model_response}")

    print(type(answer), type(model_response))

    # Check if the model response is correct
    if answer_type == 'coordinates':
        coord = ast.literal_eval(answer)
        bbox = ast.literal_eval(model_response)
        print(f"Answer: {coord}")
        # Check if answer is in bbox
        if coord[0] >= bbox[0] and coord[1] >= bbox[1] and coord[2] <= bbox[2] and coord[3] <= bbox[3]:
            correct_answers[answer_type] += 1
    else:
        if model_response == answer:
            correct_answers[answer_type] += 1
    
    questions[answer_type] += 1

# Get statistics
for prompt in PROMPTS:
    print(f"Prompt: {prompt}")
    print(f"Correct answers: {correct_answers[prompt]}")
    print(f"Total questions: {questions[prompt]}")
    # Division by zero check
    if questions[prompt] == 0:
        print(f"Accuracy: 0")
    else:
        print(f"Accuracy: {correct_answers[prompt] / questions[prompt]}")
    print("\n\n")

# Get the overall statistics
total_correct = sum(correct_answers.values())
total_questions = sum(questions.values())
print(f"Total correct answers: {total_correct}")
print(f"Total questions: {total_questions}")
# Division by zero check
if total_questions == 0:
    print(f"Total accuracy: 0")
else:
    print(f"Total accuracy: {total_correct / total_questions}")
print("\n")
