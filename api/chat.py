import google.generativeai as genai
import os
from typing import Any
from flask import Request, jsonify

# Configure a API key do Gemini (deve estar definida como variável de ambiente no painel da Vercel)
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "GEMINI_API_KEY"))

# Carrega o modelo Gemini
model = genai.GenerativeModel("gemini-pro")

def handler(request: Request) -> Any:
    try:
        # Pega os dados enviados no corpo da requisição
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"reply": "Mensagem vazia recebida."}), 400

        # Gera a resposta com o modelo Gemini
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
