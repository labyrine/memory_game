import pygame
import os
import random
from sprites.card import Card 

def create_cards(current_directory, width, height):
    image_names = ["apple.png", "bird.png", "butterfly.png", "campfire.png", "car.png", "cherry.png", "donut.png", "fish.png", "flower.png", "flower1.png", "heart.png", "hotairballoon.png", "house.png", "icecream.png", "mess.png", "night.png", "octopus.png", "snail.png", "tree1.png", "tree2.png"]
    
    image_paths = [os.path.join(current_directory, "assets", name) for name in image_names]
    
    card_images = image_paths * 2
    
    random.shuffle(card_images)
    
    box_width = width // 8
    box_height = (height - 100) // 5
    
    all_cards = pygame.sprite.Group()
    
    # Generated code starts
    for row in range(5):
        for col in range(8):
            index = row * 8 + col 
            # Generated code ends
            x = 10 + col * box_width
            y = 110 + row * box_height
            card = Card(card_images[index], os.path.join(current_directory, "assets", "back.png"), x, y)
            all_cards.add(card)
    
    return all_cards