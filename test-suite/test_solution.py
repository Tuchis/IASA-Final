# Test suite of representations of the solution to the problem

import pandas as pd
import os
from openai_client import OpenAI_Client

# Read train data
train_data_path = 'IASA_Champ_Final'
train_data_file = 'ui_questions_train.tsv'

train_data = pd.read_csv(os.path.join(train_data_path, train_data_file), sep='\t')

print(train_data.head(5))

# Get our image representations
...

# Init OpenAI client
# openai_client = OpenAI_Client()

for row_ind, row in train_data.iterrows():
    app_bundle, app_name, screen_id, question, answer, answer_type = row
    # screen_representation = row['screen_representation']
    print(answer_type, question)

    # Find the representation of the screen
    screen_representation = ...

    # Get the model response
    model_response = openai_client.get_model_response(
        answer_type,
        question, 
        screen_representation
    )