# # Test suite of representations of the solution to the problem

# import pandas as pd
# import os
# import json
# import ast
# from openai_client import OpenAI_Client

# # Read train data
# train_data_path = '../IASA_Champ_Final'
# train_data_file = 'ui_questions_train.tsv'

# # Path to the sample file (comment or delete for the final solution)
# # train_data_file = 'ui_questions_train_test.tsv'

# train_data = pd.read_csv(os.path.join(train_data_path, train_data_file), sep='\t')

# for type_of_data in ['number', 'yes/no', 'coordinates', 'string']:
#     print(f"Type of data: {type_of_data}")
#     for row_number, row in train_data[train_data['Answer Type'] == type_of_data].iterrows():
#         print(row['Question'])
#     print("\n\n\n\n")

from openai import OpenAI

# client = OpenAI(api_key="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")

# # openai.api_key = "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"

# response = client.chat.completions.create(
#   model="gpt-4-vision-preview",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )

# print(response.choices[0])