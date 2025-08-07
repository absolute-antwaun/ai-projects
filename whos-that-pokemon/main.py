# main.py
import pygame
import sys
import os
import json
from utils import create_silhouette, load_names, normalize_name, random_pokemon_ids, SPRITE_DIR
from PIL import Image
import io

# Config
SPRITE_DIR = "assets/sprites"
META_FILE = "assets/names.json"
WINDOW_SIZE = (640, 480)
SIL_SIZE = (300, 300)
ROUNDS = 10

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Who's That Pokémon?")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 24)
BIGFONT = pygame.font.SysFont("arial", 36)

# Load mapping
if os.path.exists(META_FILE):
    with open(META_FILE, "r") as f:
        id_to_name = json.load(f)
else:
    print("Missing names metadata. Run download_sprites.py first.")
    id_to_name = {}

def pil_to_surface(pil_img):
    """Convert PIL image to pygame Surface"""
    mode = pil_img.mode
    size = pil_img.size
    data = pil_img.tobytes()
    return pygame.image.fromstring(data, size, mode).convert_alpha()

def load_sprite_surface(pid):
    path = os.path.join(SPRITE_DIR, f"{pid}.png")
    if not os.path.exists(path):
        return None
    pil = Image.open(path).convert("RGBA")
    pil = pil.resize(SIL_SIZE, Image.LANCZOS)
    return pil_to_surface(pil)

def load_silhouette_surface(pid):
    path = os.path.join(SPRITE_DIR, f"{pid}.png")
    pil = create_silhouette(path, output_size=SIL_SIZE)
    return pil_to_surface(pil)

def draw_text_center(text, y, font=FONT, color=(255,255,255)):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WINDOW_SIZE[0]//2, y))
    screen.blit(surf, rect)

def game_loop():
    score = 0
    round_no = 0

    while round_no < ROUNDS:
        round_no += 1
        pid = random_pokemon_ids(1)[0]
        real_name = id_to_name.get(pid, pid)
        sil_surf = load_silhouette_surface(pid)
        sprite_surf = load_sprite_surface(pid)

        input_text = ""
        guessed = False
        revealed = False
        result_text = ""

        # Guess phase
        while not revealed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        # submit guess
                        guessed_name = normalize_name(input_text)
                        correct_name = normalize_name(real_name)
                        if guessed_name == correct_name:
                            result_text = f"Correct! It was {real_name.title()}."
                            score += 1
                        else:
                            result_text = f"Wrong — it was {real_name.title()}."
                        revealed = True
                    else:
                        # append char (limit length)
                        if len(input_text) < 30 and event.unicode.isprintable():
                            input_text += event.unicode

            screen.fill((12, 12, 30))  # dark sci-fi background
            draw_text_center("Who's That Pokémon?", 50, BIGFONT)
            # draw silhouette centered
            if sil_surf:
                rect = sil_surf.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2 - 20))
                screen.blit(sil_surf, rect)
            # draw input box
            pygame.draw.rect(screen, (40,40,60), (120, 400, 400, 36))
            txt_surf = FONT.render(input_text, True, (255,255,255))
            screen.blit(txt_surf, (130, 408))
            draw_text_center(f"Round {round_no}/{ROUNDS}  Score: {score}", 20)
            draw_text_center("Type your guess and press Enter", WINDOW_SIZE[1]-30, FONT)
            pygame.display.flip()
            clock.tick(30)

        # reveal phase (show sprite + message)
        reveal_timer = 0
        while reveal_timer < 120:  # show ~4 seconds at 30 FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
            screen.fill((6,6,20))
            draw_text_center(result_text, 40, BIGFONT)
            if sprite_surf:
                rect = sprite_surf.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2 + 10))
                screen.blit(sprite_surf, rect)
            draw_text_center(f"Score: {score}", WINDOW_SIZE[1]-30)
            pygame.display.flip()
            clock.tick(30)
            reveal_timer += 1

    # End screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
        screen.fill((0,0,0))
        draw_text_center("Game Over", 120, BIGFONT)
        draw_text_center(f"Final Score: {score}/{ROUNDS}", 200, FONT)
        draw_text_center("Press Enter or Esc to quit", 360, FONT)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()