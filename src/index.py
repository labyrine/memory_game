import sys
import os
import pygame
from services.memory_game_setup import MemoryGameSetUp
from ui.game_display import draw_backround


current_directory = os.path.dirname(os.path.abspath(__file__))


WIDTH = 800
HEIGHT = 600


def main():
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    lavender = (230, 230, 250)

    font = pygame.font.SysFont("verdana", 56)

    setup = MemoryGameSetUp(current_directory, WIDTH, HEIGHT)
    pairs_count = len(setup.all_cards) // 2
    points = 0

    cards_turned = []
    # Generated code starts
    flip_timer = pygame.time.get_ticks()
    # Generated code ends
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Muistipeli")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for card in setup.all_cards:
                    if card.card_chosen(mouse_x, mouse_y) and len(cards_turned) < 2 and card not in cards_turned:
                        card.flip()
                        cards_turned.append(card)

        if len(cards_turned) == 2:
            # Generated code starts
            if pygame.time.get_ticks() - flip_timer > 3000:
                # Generated code ends
                if cards_turned[0].is_matching(cards_turned[1]):
                    points += 1
                    cards_turned[0].delete_found()
                    cards_turned[1].delete_found()
                    cards_turned = []
                    if points == pairs_count:
                        pygame.quit()
                        sys.exit()
                elif not cards_turned[0].is_matching(cards_turned[1]):
                    cards_turned[0].flip()
                    cards_turned[1].flip()
                    cards_turned = []
                else:
                    pass
                # Generated code starts
                flip_timer = pygame.time.get_ticks()
                # Generated code ends

        draw_backround(screen, black, white, lavender, WIDTH, HEIGHT, font)

        setup.all_cards.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()
