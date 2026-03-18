import tkinter as tk
from tkinter import scrolledtext
from core.scanner import analyze_site
from core.ports import scan_ports
from core.ai import perguntar_ia
from urllib.parse import urlparse
import threading

def iniciar_interface():
    root = tk.Tk()
    root.title("CLEITAN OS")

    output = scrolledtext.ScrolledText(root)
    output.pack()

    def log(msg):
        output.insert(tk.END, msg + "\n")
        output.see(tk.END)

    entry = tk.Entry(root)
    entry.pack(fill="x")

    def analisar():
        url = entry.get()
        threading.Thread(target=analyze_site, args=(url, log)).start()

    def portas():
        host = urlparse(entry.get()).netloc
        threading.Thread(target=scan_ports, args=(host, log)).start()

    def ia():
        resposta = perguntar_ia(entry.get())
        log(resposta)

    tk.Button(root, text="ANALISAR", command=analisar).pack()
    tk.Button(root, text="PORTS", command=portas).pack()
    tk.Button(root, text="IA", command=ia).pack()

    root.mainloop()