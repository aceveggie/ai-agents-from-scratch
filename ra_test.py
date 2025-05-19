#Hardcoded Agent
from openai_module import generate_text_basic
from prompts import react_system_prompt

city_list = ['San Francisco', 'Paris', 'London', 'New York', 'Toronto', 'Seattle']

for city in city_list:
    prompt = f"""Should I take an umbrella when going out today in {city}?"""
    response = generate_text_basic(prompt, model="gpt-4", system_prompt=react_system_prompt)
    print(f'City: {city}, Response: {response}')
    print('----------------------')
