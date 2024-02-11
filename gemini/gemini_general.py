import vertexai
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)
import http.client
import typing
import urllib.request
import IPython.display
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps
PROJECT_ID = "primeval-beaker-413911"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
vertexai.init(project=PROJECT_ID, location=LOCATION)

def print_multimodal_prompt(contents: list):
    """
    Given contents that would be sent to Gemini,
    output the full multimodal prompt for ease of readability.
    """
    for content in contents:
        if isinstance(content, Image):
            display_images([content])
        elif isinstance(content, Part):
            url = get_url_from_gcs(content.file_data.file_uri)
            IPython.display.display(load_image_from_url(url))
        else:
            print(content)

def generate_description():
    multimodal_model = GenerativeModel("gemini-pro-vision")
    image = Image.load_from_file("photo_2024-02-10 14.32.28.jpeg")

    prompt = "You have a UI interface photo. This photo has buttons, text inputs etc. Give all the text from picture, capturing it's relativeness. Describe all meaningful elements of the UI interface. For example, you can describe the buttons, text inputs, etc. Also analyze the structure of page and name elements in it"

    contents = [image, prompt]

    responses = multimodal_model.generate_content(contents, stream=True)

    print("-------Prompt--------")
    print_multimodal_prompt(contents)

    print("\n-------Response--------")
    general = ''
    for response in responses:
        general += response.text

    #prompts.append([prompt, general])
    prompt1 = f"Ask 10 detailed questions about status of elements(is button active, how many buttons are active), count of buttons, inputs etc,given this desctiption of display: {general}. Do not make questions repetitive"
    questions = multimodal_model.generate_content([prompt1], stream=True)
    response = ""
    for qe in questions:
        response += qe.text

    query = []
    for gg in response.split("\n"):
        query.append(gg)
    #prompts.append([prompt1, response])

    prompt1 = f"Ask 10 questions about names of elements mentioned, ask for current tab, page, active buttons, what is selected menu page, given this desctiption of display: {general}. Do not make questions repetitive"
    questions = multimodal_model.generate_content([prompt1], stream=True)
    response = ""
    for qe in questions:
        response += qe.text

    #prompts.append([prompt1, response])
    for gg in response.split("\n"):
        query.append(gg)

    description = general
    description += '\n'

    prompt3 = "You have a UI interface photo. This photo has buttons, text inputs etc."

    for que in query:
        description += que
        answers = multimodal_model.generate_content([image,prompt3 + ". " +que], stream=True)
        for ans in answers:
            description += ans.text
        description += '\n'
    print(description)
