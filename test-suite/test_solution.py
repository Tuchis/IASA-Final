# Test suite of representations of the solution to the problem

import pandas as pd
import os
import json
from openai_client import OpenAI_Client

# Read train data
train_data_path = 'IASA_Champ_Final'
train_data_file = 'ui_questions_train.tsv'

train_data = pd.read_csv(os.path.join(train_data_path, train_data_file), sep='\t')

print(train_data.head(5))

# Image representations folder
image_representations_folder = "results"

def get_screen_representation(app_name, screen_id):
    path = os.path.join(image_representations_folder, app_name, screen_id)
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
    # screen_representation = row['screen_representation']
    print(answer_type, question)

    # Find the representation of the screen
    screen_representation = get_screen_representation(app_name, screen_id)

    # Get the model response
    model_response = openai_client.get_model_response(
        answer_type,
        question, 
        screen_representation
    )

    # Check if the model response is correct
    if model_response == answer:
        correct_answers[answer_type] += 1
    
    questions[answer_type] += 1

# Get statistics
for prompt in PROMPTS:
    print(f"Prompt: {prompt}")
    print(f"Correct answers: {correct_answers[prompt]}")
    print(f"Total questions: {questions[prompt]}")
    print(f"Accuracy: {correct_answers[prompt] / questions[prompt]}")
    print("\n")

# Get the overall statistics
total_correct = sum(correct_answers.values())
total_questions = sum(questions.values())
print(f"Total correct answers: {total_correct}")
print(f"Total questions: {total_questions}")
print(f"Total accuracy: {total_correct / total_questions}")
print("\n")
