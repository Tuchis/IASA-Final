import base64
import requests

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = "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"

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Replace 'path_to_your_image.jpg' with the path to your actual image file
# image_path = "/home/kuzhum/IASA/IASA-Final-Vlad/test-suite/ClearVPN-1707081884.62.png"
# base64_image = encode_image(image_path)

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {api_key}"
# }

# prompt = "You have a photo of UI interface of an app. Describe every element of UI. Include all buttons and text fields. Do not talk about color, style etc"

# payload = {
#     "model": "gpt-4-vision-preview",
#     "messages": [
#       {
#         "role": "user",
#         "content": [
#           {"type": "text", "text": prompt},
#           {
#             "type": "image_url",
#             "image_url": {
#               "url": f"data:image/jpeg;base64,{base64_image}"
#             }
#           }
#         ]
#       }
#     ],
#     "max_tokens": 500
# }

# # Make the API request and print out the response
# response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
# print(response.json())

def gpt4v_response(image_path, prompt, max_tokens=500):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
        {
            "role": "user",
            "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
            ]
        }
        ],
        "max_tokens": max_tokens
    }

    # Make the API request and print out the response
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()