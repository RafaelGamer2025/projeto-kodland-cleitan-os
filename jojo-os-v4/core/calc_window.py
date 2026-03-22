import tkinter as tk
from ui.jojo_theme import JoJoTheme
import os
from pygame import mixer 
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageGrab

def localizar_pasta_soms():
    """Busca a pasta 'soms' subindo os níveis de diretório até encontrar"""
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        tentativa = os.path.join(diretorio_atual, "soms")
        if os.path.exists(tentativa): 
            return tentativa
        diretorio_atual = os.path.dirname(diretorio_atual)
    return None

class JoJoCalc:
    def __init__(self, master):
        self.master = master
        self.master.title("JOJO CALCULATOR // STAR PLATINUM")
        self.master.geometry("400x600")
        self.master.configure(bg=JoJoTheme.BLACK)

        # Referência para a janela principal do SISTEMA (o root do JoJoOS)
        self.system_root = self.master.winfo_toplevel()

        self.click_sound = None
        self.success_sound = None 
        self.error_sound = None   
        self.hold_sound = None    
        
        self.hold_job = None 
        self.was_held = False 
        self.ee_activated = False 

        # Cores para o efeito negativo
        self.neg_black = "#ffffff"
        self.neg_gold = "#005aff" 
        self.neg_purple = "#a0ff5f" 
        self.neg_pink = "#00ffbf" 

        self.canvas_overlay = None
        self.inverted_tk = None
        self.overlay_image = None
        self.radius = 0

        try:
            mixer.init()
            pasta = localizar_pasta_soms()
            if pasta:
                self.click_sound = mixer.Sound(os.path.join(pasta, "ora-jotaro.wav"))
                self.success_sound = mixer.Sound(os.path.join(pasta, "tusk-chimimi.wav"))
                self.error_sound = mixer.Sound(os.path.join(pasta, "error.wav")) 
                self.hold_sound = mixer.Sound(os.path.join(pasta, "star-platinum-zw.wav"))
                
                if self.success_sound: self.success_sound.play()
        except Exception as e:
            print(f"Erro no mixer: {e}")

        self.result_var = tk.StringVar()
        self.buttons_list = [] 
        self.create_widgets()

    def play_sound(self, sound_type):
        try:
            if sound_type == "click" and self.click_sound: self.click_sound.play()
            elif sound_type == "success" and self.success_sound: self.success_sound.play()
            elif sound_type == "error" and self.error_sound: self.error_sound.play()
            elif sound_type == "hold" and self.hold_sound: self.hold_sound.play()
        except: pass

    def stop_time_effect(self):
        """Efeito ZA WARUDO: Captura o sistema todo e expande o círculo negativo"""
        if self.ee_activated: return
        self.ee_activated = True
        
        self.play_sound("hold")

        # 1. Pegar geometria do sistema (Root)
        x = self.system_root.winfo_rootx()
        y = self.system_root.winfo_rooty()
        w = self.system_root.winfo_width()
        h = self.system_root.winfo_height()

        # 2. Print de todas as janelas e inversão
        screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))
        self.overlay_image = ImageOps.invert(screenshot.convert("RGB"))

        # 3. Criar o Canvas sobre o ROOT do sistema
        self.canvas_overlay = tk.Canvas(self.system_root, width=w, height=h, 
                                      highlightthickness=0, bg="black")
        self.canvas_overlay.place(x=0, y=0)
        
        # --- SOLUÇÃO TÉCNICA PARA O ERRO ---
        # Forçamos o levantamento do widget usando a classe base Misc para evitar o erro de argumentos do Canvas
        tk.Misc.tkraise(self.canvas_overlay)

        self.radius = 10
        self.animate_expansion(w, h)

    def animate_expansion(self, w, h):
        max_radius = (w**2 + h**2)**0.5
        
        if self.radius < max_radius:
            self.radius += 50 # Aumentei a velocidade para ser mais responsivo
            
            mask = Image.new('L', (w, h), 0)
            draw = ImageDraw.Draw(mask)
            cx, cy = w // 2, h // 2
            draw.ellipse((cx - self.radius, cy - self.radius, 
                          cx + self.radius, cy + self.radius), fill=255)
            
            current_frame = Image.new('RGBA', (w, h), (0,0,0,0))
            current_frame.paste(self.overlay_image, (0, 0), mask=mask)
            
            self.inverted_tk = ImageTk.PhotoImage(current_frame)
            self.canvas_overlay.delete("all")
            self.canvas_overlay.create_image(0, 0, image=self.inverted_tk, anchor="nw")
            
            # Usamos master.after para não travar a thread
            self.master.after(10, lambda: self.animate_expansion(w, h))
        else:
            self.apply_negative_ui()
            self.master.after(4000, self.restore_colors)

    def apply_negative_ui(self):
        """Inverte visualmente os botões por baixo do overlay"""
        self.master.configure(bg=self.neg_black)
        self.display.configure(bg="#e5e5e5", fg=self.neg_gold)
        for btn, char in self.buttons_list:
            neg_bg = self.neg_purple if char.isdigit() else self.neg_pink
            btn.configure(bg=neg_bg, fg=self.neg_black)

    def restore_colors(self):
        if self.canvas_overlay:
            self.canvas_overlay.destroy()
            self.canvas_overlay = None
            
        self.master.configure(bg=JoJoTheme.BLACK)
        self.display.configure(bg="#1a1a1a", fg=JoJoTheme.GOLD)
        for btn, char in self.buttons_list:
            orig_bg = JoJoTheme.PURPLE if char.isdigit() else JoJoTheme.PINK
            btn.configure(bg=orig_bg, fg=JoJoTheme.GOLD)
        
        self.ee_activated = False

    def trigger_hold(self):
        self.was_held = True
        self.stop_time_effect()

    def on_press(self, char):
        self.was_held = False
        self.hold_job = self.master.after(210, self.trigger_hold)

    def on_release(self, char):
        if self.hold_job:
            self.master.after_cancel(self.hold_job)
            self.hold_job = None
        if not self.was_held:
            self.on_button_click(char)

    def create_widgets(self):
        self.display = tk.Entry(self.master, textvariable=self.result_var, font=("Impact", 32), 
                           bg="#1a1a1a", fg=JoJoTheme.GOLD, bd=5, relief="sunken", justify='right')
        self.display.pack(expand=True, fill='both', padx=10, pady=10)

        button_frame = tk.Frame(self.master, bg=JoJoTheme.BLACK)
        button_frame.pack(expand=True, fill='both')

        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', 'C', '=', '+']

        row, col = 0, 0
        for button in buttons:
            bg_color = JoJoTheme.PURPLE if button.isdigit() else JoJoTheme.PINK
            btn = tk.Button(button_frame, text=button, font=("Impact", 20), 
                            bg=bg_color, fg=JoJoTheme.GOLD, bd=3, relief="raised")
            
            btn.bind("<ButtonPress-1>", lambda e, b=button: self.on_press(b))
            btn.bind("<ButtonRelease-1>", lambda e, b=button: self.on_release(b))
            
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            self.buttons_list.append((btn, button)) 
            col += 1
            if col > 3: col = 0; row += 1

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if self.ee_activated: return
        if char == 'C':
            self.play_sound("click")
            self.result_var.set("")
        elif char == '=':
            try:
                self.result_var.set(str(eval(self.result_var.get())))
                self.play_sound("success")
            except:
                self.result_var.set("MUDA MUDA!")
                self.play_sound("error")
        else:
            self.play_sound("click")
            self.result_var.set(self.result_var.get() + char)