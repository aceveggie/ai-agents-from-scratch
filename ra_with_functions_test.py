
from openai_module import generate_text_basic
from prompts import react_system_prompt
from sample_functions import get_weather
from json_helpers import extract_json


#Available actions are:
available_actions = {
    "get_weather": get_weather
}

city_list = ['San Francisco', 'Paris', 'London', 'New York', 'Toronto', 'Seattle']

for city in city_list:
    prompt = f"""Should I take an umbrella when going out today in {city}?"""
    response = generate_text_basic(prompt, model="gpt-4", system_prompt=react_system_prompt)
    print(f'City: {city}, Response: {response}')
    # we want to instruct the model to call the action or the function
    json_function = extract_json(response)
    print(f'extracted json functions {json_function}')

    if json_function:
        function_name = json_function['function_name']
        function_parms = json_function['function_parms']
        if function_name not in available_actions:
            print(f"Unknown action: {function_name}: {function_parms}")
        print(f'-- running function {function_name} with params {function_parms}')
        action_function = available_actions[function_name]
        # call the function
        result = action_function(**function_parms)
        function_result_message = f'Action result: {result}'
        print(function_result_message)
        print('---')
    print('----------------------')
