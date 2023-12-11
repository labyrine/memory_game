import sys
import pygame


# Generated code starts
class StartScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self):
        font = pygame.font.SysFont("verdana", 36)
        guide1_text = font.render(
            "Valitse pelaajien määrä yhdestä kolmeen", True, (255, 255, 255))
        text_rect1 = guide1_text.get_rect(
            center=(self.width // 2, self.height // 2-20))
        guide2_text = font.render(
            "numeronäppäimillä 1, 2 ja 3", True, (255, 255, 255))
        text_rect2 = guide2_text.get_rect(
            center=(self.width // 2, self.height // 2+20))

        self.screen.blit(guide1_text, text_rect1)
        self.screen.blit(guide2_text, text_rect2)
        pygame.display.flip()

        num_players = None
        while num_players not in [1, 2, 3]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        num_players = 1
                    elif event.key == pygame.K_2:
                        num_players = 2
                    elif event.key == pygame.K_3:
                        num_players = 3

        return num_players
# Generated code ends
