from openai_module import generate_text_basic, generate_text_with_conversation
import os

prompt = 'What is the capital of France?'
response = generate_text_basic(prompt)
print(response)