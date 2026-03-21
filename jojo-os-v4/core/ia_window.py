import tkinter as tk
from tkinter import scrolledtext
from google import genai
import os
from dotenv import load_dotenv
import threading
from ui.jojo_theme import JoJoTheme

# Carrega a chave do arquivo .env
load_dotenv()
api_key = os.getenv("GEMINI_KEY")

# Configura o novo cliente do Gemini
client = genai.Client(api_key=api_key) if api_key else None

def abrir_janela_ia(root_principal):
    janela_ia = tk.Toplevel(root_principal)
    janela_ia.title("JOJO-OS // HEAVEN'S DOOR AI")
    janela_ia.geometry("700x600")
    janela_ia.configure(bg=JoJoTheme.BLACK)

    # Título estilizado
    tk.Label(janela_ia, text="📖 HEAVEN'S DOOR", font=("Impact", 24), 
             bg=JoJoTheme.BLACK, fg=JoJoTheme.GOLD).pack(pady=10)

    chat_box = scrolledtext.ScrolledText(janela_ia, bg="#1A1A1A", fg=JoJoTheme.WHITE, 
                                        font=("Courier New", 12), wrap=tk.WORD,
                                        insertbackground=JoJoTheme.GOLD)
    chat_box.pack(padx=20, pady=10, fill="both", expand=True)
    chat_box.config(state=tk.DISABLED)

    entrada_usuario = tk.Entry(janela_ia, bg="#2A2A2A", fg=JoJoTheme.PINK, 
                              font=("Impact", 14), insertbackground=JoJoTheme.GOLD,
                              bd=3, relief="sunken")
    entrada_usuario.pack(padx=20, pady=10, fill="x")

    def enviar_mensagem():
        pergunta = entrada_usuario.get()
        if pergunta.strip():
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, f"👤 [JOJO]: {pergunta}\n", "user")
            chat_box.tag_config("user", foreground=JoJoTheme.PINK)
            entrada_usuario.delete(0, tk.END)
            
            if not client:
                chat_box.insert(tk.END, "❌ [ERRO]: GEMINI_KEY não encontrada no .env!\n\n")
                chat_box.config(state=tk.DISABLED)
                chat_box.see(tk.END)
                return

            def processar_ia():
                try:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash", 
                        contents=pergunta
                    )
                    chat_box.config(state=tk.NORMAL)
                    chat_box.insert(tk.END, f"✒️ [HEAVEN'S DOOR]: {response.text}\n\n", "ai")
                    chat_box.tag_config("ai", foreground=JoJoTheme.GOLD)
                except Exception as e:
                    chat_box.config(state=tk.NORMAL)
                    chat_box.insert(tk.END, f"💥 [KIRA QUEEN]: {str(e)}\n\n")
                
                chat_box.config(state=tk.DISABLED)
                chat_box.see(tk.END)

            threading.Thread(target=processar_ia).start()

    btn_enviar = tk.Button(janela_ia, text="WRYYYYYYY! (ENVIAR)", command=enviar_mensagem, 
                          bg=JoJoTheme.PURPLE, fg=JoJoTheme.GOLD, font=("Impact", 14, "bold"),
                          activebackground=JoJoTheme.PINK, activeforeground=JoJoTheme.WHITE)
    btn_enviar.pack(pady=15)
    
    # Atalho ENTER
    entrada_usuario.bind("<Return>", lambda e: enviar_mensagem())
