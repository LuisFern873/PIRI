import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

inicial_prompt = "Actúa como un asistente virtual."

def chat_with_assistant(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # O el modelo más reciente disponible
        messages=[
            {"role": "system", "content": inicial_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

user_input = "¿Cómo está el clima hoy?"
assistant_response = chat_with_assistant(user_input)
print(assistant_response)
