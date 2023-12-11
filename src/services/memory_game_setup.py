import os
import random
import pygame
from sprites.card import Card


class MemoryGameSetUp:
    def __init__(self, directory_now, width, height, num_players):
        self.WIDTH = width
        self.HEIGHT = height
        self.current_directory = directory_now
        self.all_cards = pygame.sprite.Group()
        self.num_players = num_players
        self.current_player = 1
        self.scores = [0] * self.num_players

        self._initialize_sprites(directory_now, width, height)

    def _initialize_sprites(self, current_directory, width, height):
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
