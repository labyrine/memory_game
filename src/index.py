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

cards_turned = []
# Generated code starts
processing_cards = False
flip_timer = pygame.time.get_ticks()
# Generated code ends

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Generated code starts
        if not processing_cards and event.type == pygame.MOUSEBUTTONDOWN:
            # Generated code ends
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for card in all_cards:
                if card.card_chosen(mouse_x, mouse_y) and len(cards_turned) < 2 and card not in cards_turned:
                    card.flip()
                    cards_turned.append(card)
            # Generated code starts
            if len(cards_turned) == 2:
                processing_cards = True
            # Generated code ends

    if len(cards_turned) == 2:
        # Generated code starts
        if pygame.time.get_ticks() - flip_timer > 3000:
            # Generated code ends
            cards_turned[0].flip()
            cards_turned[1].flip()
            cards_turned = []
            # Generated code starts
            processing_cards = False
            flip_timer = pygame.time.get_ticks()
            # Generated code ends

    draw_backround(screen, black, white, lavender, WIDTH, HEIGHT, font)

    all_cards.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
