import pygame

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