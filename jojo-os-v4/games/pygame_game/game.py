import pygame
import os
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cleitan-OS Game")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Carregar imagens
def load_images():
    images = []
    image_folder = os.path.join("assets", "imagen")
    for filename in os.listdir(image_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img = pygame.image.load(os.path.join(image_folder, filename))
            images.append(img)
    return images

# Carregar sons
def load_sounds():
    sounds = {}
    sound_folder = os.path.join("assets", "sounds")
    # Se assets/sounds não for um diretório (ex.: arquivo placeholder), usar a pasta comum 'soms'
    if not os.path.isdir(sound_folder):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        sound_folder = os.path.join(base_dir, "soms")

    if os.path.isdir(sound_folder):
        for filename in os.listdir(sound_folder):
            if filename.endswith(".wav") or filename.endswith(".mp3") or filename.endswith(".ogg"):
                try:
                    sound = pygame.mixer.Sound(os.path.join(sound_folder, filename))
                    sounds[filename] = sound
                except Exception:
                    pass
    return sounds

# Função principal do jogo
def main():
    running = True
    clock = pygame.time.Clock()
    images = load_images()
    sounds = load_sounds()

    # Tocar um som de fundo se houver
    if "background.wav" in sounds:
        sounds["background.wav"].play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preencher a tela com preto
        screen.fill(BLACK)

        # Desenhar imagens aleatórias na tela
        if images:
            img = random.choice(images)
            screen.blit(img, (random.randint(0, WIDTH - img.get_width()), random.randint(0, HEIGHT - img.get_height())))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()