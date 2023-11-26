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

box_width = width // 8
box_height = (height - 100) // 5

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path, back_image_path, pos_x, pos_y, card_width=80, card_height=80):
        super().__init__()
        self.picture_image = pygame.transform.scale(pygame.image.load(image_path), (card_width, card_height))
        self.back_image = pygame.transform.scale(pygame.image.load(back_image_path), (card_width, card_height))
        self.image = self.back_image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.is_open = False

    def card_chosen(self, mouse_location):
        if self.rect.collidepoint(mouse_location):
            self.flip()

    def flip(self):
        if self.is_open:
            self.is_open = False
            self.image = self.picture_image
        else:
            self.is_open = True
            self.image = self.back_image

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

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Muistipeli")

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in all_cards:
                card.card_chosen(mouse_pos)

    draw_backround()

    all_cards.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
