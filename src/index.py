import pygame
import sys
import os
from services.card_service import create_cards

pygame.init()

current_directory = os.path.dirname(os.path.abspath(__file__))

width = 800
height = 600

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)

font = pygame.font.SysFont("verdana", 56)

all_cards = create_cards(current_directory, width, height)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Muistipeli")

def draw_backround():
    text_box = pygame.draw.rect(screen, black, [0, 0, width, 100])
    title = font.render("Muistipeli", True, white)
    screen.blit(title, (10, 20))
    game_table = pygame.draw.rect(screen, lavender, [0, 100, width, height-100], 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in all_cards:
                card.card_chosen(mouse_pos)

    draw_backround()

    all_cards.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)