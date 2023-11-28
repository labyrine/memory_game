import sys
import os
import pygame
from services.card_service import create_cards
from ui.game_display import draw_backround

pygame.init()

current_directory = os.path.dirname(os.path.abspath(__file__))

WIDTH = 800
HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)

font = pygame.font.SysFont("verdana", 56)

all_cards = create_cards(current_directory, WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Muistipeli")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in all_cards:
                card.card_chosen(mouse_pos)

    draw_backround(screen, black, white, lavender, WIDTH, HEIGHT, font)

    all_cards.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
