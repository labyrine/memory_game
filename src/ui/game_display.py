import pygame

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)
magneta = (255, 0, 255)


class Renderer:
    """A class that renders the screen and its objects during the game.

    Attributes:
        screen: A pygame surface.
        setup: An instance of the MemoryGameSetup class containing game setup information.
    """

    def __init__(self, screen, setup):
        """
        The constructor of the class that creates a new renderer object.

        Args:
            screen: A pygame surface.
            setup: An instance of the MemorGameSetup class containing game setup information.
        """
        self._screen = screen
        self._setup = setup
        self.width = self._setup.width
        self.height = self._setup.height

    def render(self, current_player, scores, num_players):
        """
        Renders information of the game on the screen.

        Args:
            current_player: The current player's index.
            scores: A list containing the scores of each player.
            num_players: The number of players in the game.
        """
        pygame.draw.rect(self._screen, black, [0, 0, self.width, 100])
        player1_text = "Pelaaja 1"
        player2_text = "Pelaaja 2"
        player3_text = "Pelaaja 3"

        pygame.draw.rect(
            self._screen, lavender, [0, 100, self.width, self.height-100], 0)
        self._setup.all_cards.draw(self._screen)

        if num_players == 1:
            self._draw_player_info(
                player1_text, scores[0], 325, 10, current_player == 1)

        elif num_players == 2:
            self._draw_player_info(
                player1_text, scores[0], 50, 10, current_player == 1)
            self._draw_player_info(
                player2_text, scores[1], self.width - 250, 10, current_player == 2)

        elif num_players == 3:
            self._draw_player_info(
                player1_text, scores[0], 10, 10, current_player == 1)
            self._draw_player_info(
                player2_text, scores[1], 325, 10, current_player == 2)
            self._draw_player_info(
                player3_text, scores[2], self.width - 190, 10, current_player == 3)

        pygame.display.update()

    def _draw_player_info(self, player, score, x, y, is_current_player):
        """
        Draws player information on the screen.

        Args:
            player: The player's name.
            score: The player's score.
            x: The x-coordinate for the player information.
            y: The y-coordinate for the player information.
            is_current_player: Determines whether the player is currently active.
        """
        font = pygame.font.SysFont("verdana", 36)
        # Generated code starts
        player_text = font.render(
            player, True, magneta if is_current_player else white)
        score_text = font.render(
            f"Pisteet: {score}", True, magneta if is_current_player else white)
        # Generated code ends

        self._screen.blit(player_text, (x, y))
        self._screen.blit(score_text, (x, y + 40))

    # Generated code starts
    def display_start_screen(self):
        self._screen.fill((0, 0, 0))
        font = pygame.font.SysFont("verdana", 36)
        guide1_text = font.render(
            "Valitse pelaajien määrä yhdestä kolmeen", True, (255, 255, 255))
        text_rect1 = guide1_text.get_rect(
            center=(self.width // 2, self.height // 2 - 20))
        guide2_text = font.render(
            "numeronäppäimillä 1, 2 ja 3", True, (255, 255, 255))
        text_rect2 = guide2_text.get_rect(
            center=(self.width // 2, self.height // 2 + 20))

        self._screen.blit(guide1_text, text_rect1)
        self._screen.blit(guide2_text, text_rect2)
        pygame.display.flip()
    # Generated code ends

    def display_score_screen(self, scores, num_players):
        self._screen.fill((0, 0, 0))
        font = pygame.font.SysFont("verdana", 36)
        score_text = font.render("Tulokset", True, (255, 0, 255))
        self._screen.blit(score_text, (300, 20))

        player_scores = []
        for i in range(len(scores)):
            player_number = i + 1
            player_score = scores[i]
            player_tuple = (player_score, player_number)
            player_scores.append(player_tuple)

        sorted_players = sorted(player_scores, key=lambda a: (-a[0], a[1]))

        for i in range(num_players):
            player_score, player_number = sorted_players[i]
            player_text = f"Pelaaja {player_number}"
            y_pos = 80 + i * 100
            self._draw_player_info(
                player_text, player_score, 300, y_pos, False)

        pygame.display.flip()
