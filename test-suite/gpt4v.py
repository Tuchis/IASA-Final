import base64
import requests

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = "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"

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Replace 'path_to_your_image.jpg' with the path to your actual image file
image_path = "/home/kuzhum/IASA/IASA-Final-Vlad/IASA_Champ_Final/app_data/AppStore/1707173654/App Store-1707173656.53.png"
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

prompt = "Here is an image of an app. I want you to detect all UI elements that are present in the image. For each UI element detected, I want you to provide the name of the UI element and the coordinates of the bounding box around the UI element. Also, if that UI element has some special property (it is a button, a text field, a label, etc.), I want you to provide that information as well. If there are any other details that you think are important, please include them as well."

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
    "max_tokens": 300
}

# Make the API request and print out the response
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json())