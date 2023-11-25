import pygame
import random
import sys
import os

pygame.init()

current_directory = os.path.dirname(os.path.abspath(__file__))

width = 800
height = 600

white = (255, 255, 255)
black = (0, 0, 0)
lavender = (230, 230, 250)

font = pygame.font.SysFont("verdana", 56)

image_names = ["apple.png", "bird.png", "butterfly.png", "campfire.png", "car.png", "cherry.png", "donut.png", "fish.png", "flower.png", "flower1.png", "heart.png", "hotairballoon.png", "house.png", "icecream.png", "mess.png", "night.png", "octopus.png", "snail.png", "tree1.png", "tree2.png"]

image_paths = [os.path.join(current_directory, "assets", name) for name in image_names]

card_images = image_paths * 2

random.shuffle(card_images)

card_width = width // 8
card_height = (height - 100) // 5

# AI generated code starts
grid = []
for row in range(5):
   for col in range(8):
       index = row * 8 + col
       card = {
           "image": pygame.image.load(card_images[index]),
           "rect": pygame.Rect(col * card_width, 100 + row * card_height, card_width, card_height),
       }
       grid.append(card)
# AI generated code ends

screen = pygame.display.set_mode((width, height))

def draw_backround():
    text_box = pygame.draw.rect(screen, black, [0, 0, width, 100])
    title = font.render("Muistipeli", True, white)
    screen.blit(title, (10, 20))
    game_table = pygame.draw.rect(screen, lavender, [0, 100, width, height-100], 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_backround()

    # AI generated code starts
    for card in grid:
       screen.blit(pygame.transform.scale(card["image"], (card_width, card_height)), card["rect"])
    # AI generated code ends

    pygame.display.flip()
    pygame.time.Clock().tick(60)
