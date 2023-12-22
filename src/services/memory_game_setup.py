import os
import random
import pygame
from sprites.card import Card


class MemoryGameSetUp:
    """A class that sets up the memory game with cards.

    Attributes:
        width: The width of the game window.
        height: The height of the game window.
        current_directory: The current directory of the game.
        all_cards: A pygame sprite group containing all the memory game cards.
    """

    def __init__(self, directory_now, width, height):
        """Initialize the MemoryGameSetUp with the game's dimensions and current directory.
        """

        self.width = width
        self.height = height
        self.current_directory = directory_now
        self.all_cards = pygame.sprite.Group()
        
        try:
            self._initialize_sprites(directory_now, width, height)
        except FileNotFoundError as err:
            print("FileNotFoundError while initializing sprites:", err)
        except pygame.error as err:
            print("Pygame.error while initializing sprites:", err)

    def _initialize_sprites(self, current_directory, width, height):
        """Initialize the sprites for the memory game.

        The function loads images, duplicates them, shuffles the duplicates, 
        assigns coordinates to each image, and creates a sprite group for the cards

        Args:
            width: The width of the game window for calculating cards coordinates.
            height: The height of the game window for calculating cards coordinates.
            current_directory: The current directory of the game for loading images.
        """
        
        image_names = [
            "apple.png", "bird.png", "butterfly.png", "campfire.png", "car.png",
            "cherry.png", "donut.png", "fish.png", "flower.png", "flower1.png",
            "heart.png", "hotairballoon.png", "house.png", "icecream.png", "mess.png",
            "night.png", "octopus.png", "snail.png", "tree1.png", "tree2.png"
        ]

        image_paths = [os.path.join(current_directory, "assets", name)
                       for name in image_names]

        card_images = image_paths * 2

        random.shuffle(card_images)

        box_width = width // 8
        box_height = (height - 100) // 5

        # Generated code starts
        for row in range(5):
            for col in range(8):
                index = row * 8 + col
        # Generated code ends
                x = 10 + col * box_width
                y = 110 + row * box_height
                card = Card(card_images[index], os.path.join(
                    current_directory, "assets", "back.png"), x, y)
                self.all_cards.add(card)
