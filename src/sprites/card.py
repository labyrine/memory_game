import pygame


class Card(pygame.sprite.Sprite):
    """A class that represents a card in the memory game.

    Attributes:
        picture_image: The image displayed on the front of the card.
        back_image: The image displayed on the back of the card.
        image: The current image of the card.
        rect: The rectangle representing the position and size of the card.
        rect.x: The position for x coordinate.
        rect.y: The position for y coordinate.
        is_open: A boolean passing infomration whether the card is open or closed.
    """

    def __init__(self, image_path, back_image_path, pos_x, pos_y, card_width=80, card_height=80):
        """Initialize the Card with image paths and position.
        """

        super().__init__()
        self.picture_image = pygame.transform.scale(
            pygame.image.load(image_path), (card_width, card_height))
        self.back_image = pygame.transform.scale(
            pygame.image.load(back_image_path), (card_width, card_height))
        self.image = self.back_image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.is_open = False

    def card_chosen(self, mouse_location_x, mouse_location_y):
        """Check if the given mouse coordinates are within the card.

        Args
            mouse_location_x: Mouses x coordinate.
            mouse_location_y: Mouses y coordinate.
        """

        return bool(self.rect.collidepoint(mouse_location_x, mouse_location_y))

    def flip(self):
        """Flip the card by changing its image from front to back or vice versa.
        """

        if self.is_open:
            self.is_open = False
            self.image = self.back_image
        else:
            self.is_open = True
            self.image = self.picture_image

    def is_matching(self, other_card):
        """Check if the image of this card matches the image of another card.

        Args:
            other_card: Card to compare the first selected card.
        """

        self_str = pygame.image.tostring(self.image, 'RGB')
        other_str = pygame.image.tostring(other_card.image, 'RGB')

        return self_str == other_str

    def delete_found(self):
        """Remove the card from the game when it is found.
        """

        self.kill()
