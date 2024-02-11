import json
from openai import OpenAI

class OpenAI_Client:
    def __init__(self) -> None:
        self.PROMPTS = json.load(open("/home/kuzhum/IASA/IASA-Final-Vlad/test-suite/data/prompts.json"))
        # створіть клієнт використовуючи токен вашої команди
        self.openai_client = OpenAI(api_key="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")

    def get_model_response(self, question_type, question, screen_representation):
        prompt = self.PROMPTS[question_type]
        formatted_prompt = prompt\
            .replace("<screen_representation>", screen_representation)\
            .replace("<question>", question)
        
        model_response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature=0,
            messages=[{
                "role": "user",
                "content": formatted_prompt
            }],
        )
        
        answer = json.loads(model_response.choices[0].message.content)["answer"]
        return answer