import os

def listar_programas(log):
    caminhos = ["C:\\Program Files", "C:\\Program Files (x86)"]

    for caminho in caminhos:
        try:
            for item in os.listdir(caminho):
                log(item)
        except:
            pass