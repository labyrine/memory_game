import pygame

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)
magneta = (255, 0, 255)


class Renderer:
    def __init__(self, screen, setup):
        self._screen = screen
        self._setup = setup
        self.WIDTH = self._setup.WIDTH
        self.HEIGHT = self._setup.HEIGHT

    def render(self, current_player, scores, num_players):
        pygame.draw.rect(self._screen, black, [0, 0, self.WIDTH, 100])
        player1_text = "Pelaaja 1"
        player2_text = "Pelaaja 2"
        player3_text = "Pelaaja 3"

        pygame.draw.rect(
            self._screen, lavender, [0, 100, self.WIDTH, self.HEIGHT-100], 0)
        self._setup.all_cards.draw(self._screen)

        if num_players == 1:
            self._draw_player_info(
                player1_text, scores[0], 325, 10, current_player == 1)

        elif num_players == 2:
            self._draw_player_info(
                player1_text, scores[0], 50, 10, current_player == 1)
            self._draw_player_info(
                player2_text, scores[1], self.WIDTH - 250, 10, current_player == 2)

        elif num_players == 3:
            self._draw_player_info(
                player1_text, scores[0], 10, 10, current_player == 1)
            self._draw_player_info(
                player2_text, scores[1], 325, 10, current_player == 2)
            self._draw_player_info(
                player3_text, scores[2], self.WIDTH - 190, 10, current_player == 3)

        pygame.display.update()

    def _draw_player_info(self, player, score, x, y, is_current_player):
        font = pygame.font.SysFont("verdana", 36)
        # Generated code starts
        player_text = font.render(
            player, True, magneta if is_current_player else white)
        score_text = font.render(
            f"Pisteet: {score}", True, magneta if is_current_player else white)
        # Generated code ends

        self._screen.blit(player_text, (x, y))
        self._screen.blit(score_text, (x, y + 40))
