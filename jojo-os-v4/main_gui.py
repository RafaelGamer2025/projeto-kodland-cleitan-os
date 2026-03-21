import tkinter as tk
from tkinter import messagebox
import os 
import subprocess 
from dotenv import load_dotenv

# IMPORT DO TEMA JOJO
from ui.jojo_theme import JoJoTheme
from core.ia_window import abrir_janela_ia
from core.calc_window import JoJoCalc
from ui.menacing_animation import start_menacing

# CARREGAR VARIÁVEIS
load_dotenv()

class JoJoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("JOJO-OS v4.0 // BIZARRE ADVENTURE")
        self.root.geometry("1000x700")
        self.root.configure(bg=JoJoTheme.BLACK)

        # Barra Superior Estilizada
        self.top_bar = tk.Frame(root, bg=JoJoTheme.PURPLE, height=40)
        self.top_bar.pack(side="top", fill="x")
        
        tk.Label(self.top_bar, text="⭐ JOJO-OS: GOLDEN EXPERIENCE EDITION", 
                 fg=JoJoTheme.GOLD, bg=JoJoTheme.PURPLE, 
                 font=("Impact", 14, "bold")).pack(side="left", padx=20)

        # Área de Trabalho
        self.canvas = tk.Canvas(root, bg=JoJoTheme.BLACK, highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        # Ícones com nomes de Stands/Personagens
        self.add_icon("Calculadora", "🔢", self.open_calc, 80, 80, "STAR PLATINUM")
        self.add_icon("Heaven's Door IA", "📖", self.open_ia, 250, 80, "ROHAN KISHIBE")
        self.add_icon("Menacing", "ゴ", self.open_menacing, 420, 80, "DIO BRANDO")
        self.add_icon("Killer Queen", "💣", self.open_antivirus, 80, 220, "YOSHIKAGE KIRA")
        self.add_icon("Games", "🕹️", self.run_pygame, 250, 220, "D'ARBY THE PLAYER")

    def add_icon(self, name, symbol, command, x, y, stand_name):
        # Frame para o ícone
        icon_frame = tk.Frame(self.root, bg=JoJoTheme.BLACK)
        icon_frame.place(x=x, y=y)
        
        btn = tk.Button(icon_frame, text=f"{symbol}", command=command,
                        bg=JoJoTheme.PURPLE, fg=JoJoTheme.GOLD, font=("Impact", 30),
                        bd=4, relief="raised", activebackground=JoJoTheme.PINK, 
                        activeforeground=JoJoTheme.WHITE, width=3, height=1)
        btn.pack()
        
        tk.Label(icon_frame, text=name, fg=JoJoTheme.WHITE, bg=JoJoTheme.BLACK, 
                 font=("Impact", 10)).pack()
        tk.Label(icon_frame, text=f"[{stand_name}]", fg=JoJoTheme.PINK, bg=JoJoTheme.BLACK, 
                 font=("Courier New", 8, "bold")).pack()

    def open_calc(self):
        win = tk.Toplevel(self.root)
        JoJoCalc(win)

    def open_ia(self):
        abrir_janela_ia(self.root)

    def open_menacing(self):
        # Inicia a animação menacing
        start_menacing()

    def run_pygame(self):
        try:
            # Roda o jogo como um processo separado
            subprocess.Popen(["python", "games/pygame_game/main.py"])
        except Exception as e:
            messagebox.showerror("OH NO!", f"HORY SHET! Não foi possível iniciar o jogo: {e}")

    def open_antivirus(self):
        self.antivirus_window()

    def antivirus_window(self):
        win = tk.Toplevel(self.root)
        win.title("KILLER QUEEN // BOMB SCANNER")
        win.geometry("500x400")
        win.configure(bg=JoJoTheme.BLACK)
        
        tk.Label(win, text="💣 KILLER QUEEN HAS ALREADY TOUCHED THIS FILE", 
                 fg=JoJoTheme.PINK, bg=JoJoTheme.BLACK, font=("Impact", 14)).pack(pady=20)
        
        log = tk.Text(win, bg="#1A1A1A", fg=JoJoTheme.GOLD, height=12, font=("Courier New", 10))
        log.pack(padx=20, pady=10, fill="both", expand=True)
        log.insert("1.0", "[*] Procurando por Stands inimigos...\n")
        log.insert(tk.END, "[*] SHEER HEART ATTACK HAS NO WEAKNESS!\n")
        
        tk.Button(win, text="BITE THE DUST (LIMPAR)", bg=JoJoTheme.PURPLE, fg=JoJoTheme.GOLD,
                  font=("Impact", 12), command=lambda: log.delete("1.0", tk.END)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = JoJoOS(root)
    root.mainloop()
