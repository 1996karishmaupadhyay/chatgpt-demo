import os
from dotenv import load_dotenv
from openai import OpenAI

print("Loading environment variables from .env file...")

load_dotenv();

client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"));

response = client.responses.create(
    model="gpt-6-luna",
    input="What is the name of \"prime minister Modi\"? ."
)

print(response.output_text)