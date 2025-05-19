#Hardcoded Agent
from openai_module import generate_text_basic
from sample_functions import get_weather

city = 'Seattle'

current_weather = get_weather(city=city)

prompt = f"""
Should I take an umbrella when going out today in
{city}? We know that current weather conditions is: {current_weather}?"""

response = generate_text_basic(prompt,model="gpt-4")

print(response)