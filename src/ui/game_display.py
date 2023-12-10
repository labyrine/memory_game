import pygame

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)


class Renderer:
    def __init__(self, screen, setup):
        self._screen = screen
        self._setup = setup
        self.WIDTH = self._setup.WIDTH
        self.HEIGHT = self._setup.HEIGHT

    def render(self):
        pygame.draw.rect(self._screen, black, [0, 0, self.WIDTH, 100])
        font = pygame.font.SysFont("verdana", 56)
        title = font.render("Muistipeli", True, white)
        self._screen.blit(title, (10, 20))
        pygame.draw.rect(
            self._screen, lavender, [0, 100, self.WIDTH, self.HEIGHT-100], 0)
        self._setup.all_cards.draw(self._screen)
        pygame.display.update()
