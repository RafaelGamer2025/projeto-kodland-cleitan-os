import tkinter as tk
from tkinter import ttk
from pygame import mixer
import time

# Inicializar mixer de som
mixer.init()

def tocar_som():
    sound = mixer.Sound('tusk-chimimi.wav')  # Substitua pelo caminho correto do seu arquivo de som
    ses = mixer.Sound('dio.wav')  # Substitua pelo caminho correto do seu arquivo de som
    sound.play()
    time.sleep(sound.get_length())  # Espera um pouco para o primeiro som tocar antes de tocar o segundo
    ses.play()

root = tk.Tk()
btn = ttk.Button(root, text="Tocar Som", command=tocar_som)
btn.pack(pady=20)
root.mainloop()