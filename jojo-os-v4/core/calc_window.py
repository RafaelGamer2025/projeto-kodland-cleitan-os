import tkinter as tk
from ui.jojo_theme import JoJoTheme

class JoJoCalc:
    def __init__(self, master):
        self.master = master
        self.master.title("JOJO CALCULATOR // STAR PLATINUM")
        self.master.geometry("400x600")
        self.master.configure(bg=JoJoTheme.BLACK)

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self.master, textvariable=self.result_var, font=("Impact", 32), 
                          bg="#1a1a1a", fg=JoJoTheme.GOLD, bd=5, relief="sunken", justify='right')
        display.pack(expand=True, fill='both', padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(self.master, bg=JoJoTheme.BLACK)
        button_frame.pack(expand=True, fill='both')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            color = JoJoTheme.PURPLE if button.isdigit() else JoJoTheme.PINK
            btn = tk.Button(button_frame, text=button, font=("Impact", 20), 
                           bg=color, fg=JoJoTheme.GOLD, bd=3, relief="raised",
                           activebackground=JoJoTheme.GOLD, activeforeground=JoJoTheme.BLACK,
                           command=lambda b=button: self.on_button_click(b))
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                # Substituindo eval por algo mais seguro ou mantendo a lógica original
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("MUDA MUDA!")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)
