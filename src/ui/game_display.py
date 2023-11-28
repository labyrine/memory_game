import pygame


def draw_backround(display, color1, color2, color3, screen_width, screen_height, typeface):
    text_box = pygame.draw.rect(display, color1, [0, 0, screen_width, 100])
    title = typeface.render("Muistipeli", True, color2)
    display.blit(title, (10, 20))
    game_table = pygame.draw.rect(
        display, color3, [0, 100, screen_width, screen_height-100], 0)
