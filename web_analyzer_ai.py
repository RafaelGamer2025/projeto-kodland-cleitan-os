import requests
import threading
from google import genai
import base64
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import scrolledtext
import random
import socket
import re 
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def tirar_print_site():
    url = entry.get()

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    driver.save_screenshot("print.png")
    driver.quit()

    log("[PRINT] Screenshot salvo como print.png")
# BOTÃO PARA ANALISAR HTML COM IA
def abrir_mod_menu():
    mod = tk.Toplevel(root)
    mod.title("CLEITAN MOD MENU")
    mod.geometry("400x500")
    mod.configure(bg="black")

    # deixar sempre na frente
    mod.attributes("-topmost", True)

    # ==========================
    # ARRASTAR JANELA
    # ==========================
    def start_move(event):
        mod.x = event.x
        mod.y = event.y

    def do_move(event):
        x = mod.winfo_x() + event.x - mod.x
        y = mod.winfo_y() + event.y - mod.y
        mod.geometry(f"+{x}+{y}")

    mod.bind("<Button-1>", start_move)
    mod.bind("<B1-Motion>", do_move)

    # ==========================
    # BOTÕES (MESMAS FUNÇÕES)
    # ==========================
    tk.Button(mod, text="ANALISAR", bg="black", fg="#00ff00",
              command=start_analysis).pack(fill="x")

    tk.Button(mod, text="PORT SCAN", bg="black", fg="#00ff00",
              command=start_port_scan).pack(fill="x")

    tk.Button(mod, text="IA", bg="black", fg="#00ff00",
              command=usar_ia).pack(fill="x")

    tk.Button(mod, text="CIÊNCIA", bg="black", fg="#00ff00",
              command=menu_ciencia).pack(fill="x")

    tk.Button(mod, text="JOGOS", bg="black", fg="#00ff00",
              command=menu_jogos).pack(fill="x")

    tk.Button(mod, text="ABRIR SITE", bg="black", fg="#00ff00",
              command=abrir_site).pack(fill="x")

    tk.Button(mod, text="PRINT", bg="black", fg="#00ff00",
              command=tirar_print_site).pack(fill="x")
def detect_tech(html):
    log("\n[TECH DETECT]")

    techs = {
        "WordPress": "wordpress",
        "Bootstrap": "bootstrap",
        "jQuery": "jquery",
        "React": "react",
        "Vue": "vue",
        "Angular": "angular",
        "PHP": "php",
        "Python": "django",
        "Node.js": "node"
    }

    found = []

    for nome, key in techs.items():
        if key in html.lower():
            found.append(nome)

    if found:
        for t in found:
            log(f"[TEC] {t}")
    else:
        log("Nada detectado")

def abrir_site():
    url = entry.get()
    webbrowser.open(url)
    log("[VISUAL] Abrindo site no navegador...")

def detect_tech(html):
    log("\n[TECH DETECT]")

    techs = {
        "WordPress": "wordpress",
        "Bootstrap": "bootstrap",
        "jQuery": "jquery",
        "React": "react",
        "Vue": "vue",
        "Angular": "angular",
        "PHP": "php",
        "Python": "django",
        "Node.js": "node"
    }

    found = []

    for nome, key in techs.items():
        if key in html.lower():
            found.append(nome)

    if found:
        for t in found:
            log(f"[TEC] {t}")
    else:
        log("Nada detectado")

def detect_tech(html):
    log("\n[TECH DETECT]")

    if "wordpress" in html.lower():
        log("WordPress detectado")

    if "bootstrap" in html.lower():
        log("Bootstrap detectado")

    if "jquery" in html.lower():
        log("jQuery detectado")
def find_emails(html):
    log("\n[EMAIL SCAN]")

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)

    if emails:
        for e in set(emails):
            log(f"Email: {e}")
    else:
        log("Nenhum encontrado")
def scan_ports(host):
    log(f"\n[PORT SCAN] {host}")

    portas = [21, 22, 80, 443, 3306, 8080]

    for p in portas:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, p))
            log(f"[ABERTA] {p}")
            s.close()
        except:
            log(f"[FECHADA] {p}")

# ==========================
# CONFIG
# ==========================

API_KEY = "AIzaSyBlOTzGUjR6b1WpIxiY9CKm41nNQLfRejw"  # exemplo fake
TARGET_URL = "https://learn.kodland.org/my-courses/1635/at-class"
client = genai.Client(api_key=API_KEY)
def server_info(url):
    log("\n[SERVER INFO]")

    try:
        r = requests.get(url, timeout=5)
        for k, v in r.headers.items():
            log(f"{k}: {v}")
    except:
        log("Erro ao pegar info")
def server_info(url):
    log("\n[SERVER INFO]")

    try:
        r = requests.get(url, timeout=5)
        for k, v in r.headers.items():
            log(f"{k}: {v}")
    except:
        log("Erro ao pegar info")
def usar_ia():
    pergunta = entry.get()

    def run():
        try:
            resposta = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=pergunta
            )
            log("\n[IA]")
            log(resposta.text)
        except Exception as e:
            log(f"Erro IA: {e}")

    threading.Thread(target=run, daemon=True).start()
# ==========================
# ROOT
# ==========================
root = tk.Tk()
root.title("HACKER CLEITAN SYSTEM")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# sair com ESC
root.bind("<Escape>", lambda e: root.destroy())

# ==========================
# FRAMES
# ==========================
matrix_frame = tk.Frame(root, bg="black")
boot_frame = tk.Frame(root, bg="black")
main_frame = tk.Frame(root, bg="black")

# ==========================
# MATRIX
# ==========================
canvas = tk.Canvas(matrix_frame, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

letters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"
font_size = 14
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
columns = WIDTH // font_size
drops = [0 for _ in range(columns)]

def draw_matrix():
    canvas.delete("all")

    for i in range(len(drops)):
        char = random.choice(letters)
        x = i * font_size
        y = drops[i] * font_size

        canvas.create_text(x, y, text=char, fill="#00ff00", font=("Courier", font_size))

        if y > HEIGHT or random.random() > 0.975:
            drops[i] = 0
        else:
            drops[i] += 1

    root.after(50, draw_matrix)

# ==========================
# BOOT
# ==========================
boot_text = tk.Text(boot_frame, bg="black", fg="#00ff00", font=("Courier", 14))
boot_text.pack(fill="both", expand=True)

boot_lines = [
    "Microsoft Windows [Versão Cleitan 10.0.666]",
    "(c) 2016 Hacker Systems",
    "",
    "Inicializando kernel...",
    "Carregando drivers...",
    "Hackeando Wi-Fi...",
    "Acessando servidor secreto...",
    "Liberando root...",
    "",
    "ACESSO CONCEDIDO ✔",
    "",
    "Iniciando sistema..."
]

def type_boot(i=0):
    if i >= len(boot_lines):
        root.after(1000, show_main)
        return

    line = boot_lines[i]

    for char in line:
        boot_text.insert(tk.END, char)
        boot_text.update()

    boot_text.insert(tk.END, "\n")
    root.after(200, lambda: type_boot(i + 1))

# ==========================
# MAIN SYSTEM
# ==========================
output = scrolledtext.ScrolledText(main_frame, bg="black", fg="#00ff00", font=("Courier", 10))
output.pack(fill="both", expand=True)

def log(text):
    for char in text:
        output.insert(tk.END, char)
        output.update()
        output.after(5)
    output.insert(tk.END, "\n")
    output.see(tk.END)
frame = tk.Frame(main_frame, bg="black")
frame.pack(fill="x")

entry = tk.Entry(frame, bg="black", fg="#00ff00", insertbackground="#00ff00")
entry.insert(0, TARGET_URL)
entry.pack(side="left", fill="x", expand=True)

btn1 = tk.Button(frame, text="ANALISAR SITE", bg="black", fg="#00ff00", command=lambda: start_analysis())
btn1.pack(side="left")

btn2 = tk.Button(frame, text="PORT SCAN", bg="black", fg="#00ff00", command=lambda: start_port_scan())
btn2.pack(side="left")

btn3 = tk.Button(frame, text="CIÊNCIA", bg="black", fg="#00ff00", command=lambda: menu_ciencia())
btn3.pack(side="left")

btn4 = tk.Button(frame, text="JOGOS", bg="black", fg="#00ff00", command=lambda: menu_jogos())
btn4.pack(side="left")

btn5 = tk.Button(frame, text="IA", bg="black", fg="#00ff00", command=lambda: usar_ia())
btn5.pack(side="left")

btn6 = tk.Button(frame, text="VER SITE", bg="black", fg="#00ff00", command=abrir_site)
btn6.pack(side="left")

btn7 = tk.Button(frame, text="PRINT SITE", bg="black", fg="#00ff00", command=tirar_print_site)
btn7.pack(side="left")

btn_mod = tk.Button(frame, text="MOD MENU", bg="black", fg="#00ff00", command=abrir_mod_menu)
btn_mod.pack(side="left")
# ==========================
# ANALISADOR
# ==========================
def analyze_site(url):
    log(f"\n[+] Conectando a: {url}")

    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        log(f"[ERRO] {e}")
        return

    log("[OK] Conectado")

    # LINKS
    parsed = urlparse(url)
    links = {
        urljoin(url, a['href'])
        for a in soup.find_all('a', href=True)
        if urlparse(urljoin(url, a['href'])).netloc == parsed.netloc
    }

    log("\n[SCAN] Links:")
    for l in list(links)[:10]:
        log(f" -> {l}")

    # HACKER EXTRA
    find_emails(r.text)
    detect_tech(r.text)
    server_info(url)

    # PORT SCAN
    host = urlparse(url).netloc
    scan_ports(host)
    analisar_html_com_ia(url)
    # SCRIPTS
    scripts = [urljoin(url, s['src']) for s in soup.find_all('script', src=True)]
    log("\n[SCAN] Scripts:")
    for s in scripts[:5]:
        log(f" [js] {s}")
    
def menu_jogos():
    log("\n[JOGOS]")

    log("Digite 1 para adivinhação")

    escolha = entry.get()

    if escolha == "1":
        jogo_adivinhacao_gui()
def start_analysis():
    url = entry.get()
    threading.Thread(target=analyze_site, args=(url,), daemon=True).start()
def jogo_adivinhacao_gui():
    numero = random.randint(1, 50)
    log("Adivinhe o número entre 1 e 50")

    def tentar():
        try:
            palpite = int(entry.get())

            if palpite < numero:
                log("Maior")
            elif palpite > numero:
                log("Menor")
            else:
                log("ACERTOU!")
        except:
            log("Digite número")

    btn_try = tk.Button(main_frame, text="TENTAR", command=tentar, bg="black", fg="#00ff00")
    btn_try.pack()
def menu_ciencia():
    log("\n[CIÊNCIA MODE]")

    log("1 - Massa molar")
    log("2 - pH")
    log("3 - Velocidade")
    log("4 - Força")

    escolha = entry.get()

    try:
        if escolha == "1":
            log("Digite fórmula no campo")
        elif escolha == "2":
            log("Digite valor de H+")
        elif escolha == "3":
            log("Digite distancia/tempo")
        elif escolha == "4":
            log("Digite massa/aceleração")
    except:
        log("Erro ciência")
def start_port_scan():
    url = entry.get()
    host = urlparse(url).netloc

    threading.Thread(target=scan_ports, args=(host,), daemon=True).start()
# ==========================
# TROCA DE TELAS
# ==========================
def show_matrix():
    boot_frame.pack_forget()
    main_frame.pack_forget()
    matrix_frame.pack(fill="both", expand=True)
    draw_matrix()

    root.after(4000, show_boot)

def show_boot():
    matrix_frame.pack_forget()
    main_frame.pack_forget()
    boot_frame.pack(fill="both", expand=True)
    type_boot()

def show_main():
    matrix_frame.pack_forget()
    boot_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

# ==========================
# INICIO
# ==========================
show_matrix()
root.mainloop()