import os
import pygame
from services.memory_game_setup import MemoryGameSetUp
from ui.start_display import StartScreen
from game_loop import GameLoop
from event_queue import EventQueue
from ui.game_display import Renderer
from clock import Clock


current_directory = os.path.dirname(os.path.abspath(__file__))


WIDTH = 800
HEIGHT = 600


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Muistipeli")

    home_screen = StartScreen(screen, WIDTH, HEIGHT)
    num_players = home_screen.show()

    setup = MemoryGameSetUp(current_directory, WIDTH, HEIGHT, num_players)
    event_queue = EventQueue()
    renderer = Renderer(screen, setup)
    clock = Clock()
    game_loop = GameLoop(setup, renderer, event_queue, clock)

    game_loop.start()


if __name__ == "__main__":
    main()
