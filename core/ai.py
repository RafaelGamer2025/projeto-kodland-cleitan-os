from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=API_KEY)

def perguntar_ia(texto):
    try:
        resposta = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=texto
        )
        return resposta.text
    except Exception as e:
        return f"Erro IA: {e}"