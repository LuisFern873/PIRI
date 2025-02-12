import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

PROMPT_INICIAL = "Actúa como un chatbot en español y Shipibo, brindando recomendaciones sobre embarazo, prevención de enfermedades, cuidado prenatal, alimentación, higiene y vacunación. Ofrece consejos claros y culturalmente apropiados, y explica cuándo buscar atención médica. Responde según la preferencia del usuario."

def get_chatgpt_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": PROMPT_INICIAL},
                  {"role": "user", "content": user_message}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/webhook", methods=["POST"])
def webhook():
    # Maneja mensajes entrantes de WhatsApp
    incoming_msg = request.values.get("Body", "").strip()
    response_text = get_chatgpt_response(incoming_msg)

    # Responder al usuario en WhatsApp
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
