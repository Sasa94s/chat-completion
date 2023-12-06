import openai
import os
from dotenv import load_dotenv

openai.api_key = os.environ.get("OPENAI_API_KEY")


def chat_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
