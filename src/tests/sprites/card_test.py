import unittest
from sprites.card import Card
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(current_directory, "..", "..", "assets", "apple.png")
back_image_path = os.path.join(
    current_directory, "..", "..", "assets", "back.png")


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(image_path, back_image_path, 0, 0,)

    def test_card_is_upside_down_first(self):
        self.assertFalse(self.card.is_open)

    def test_card_opens(self):
        self.card.flip()
        self.assertTrue(self.card.is_open)

    def test_flip_from_not_open_to_open(self):
        self.card.is_open = False
        self.card.flip()
        self.assertTrue(self.card.is_open)

    def test_flip_from_open_to_not_open(self):
        self.card.is_open = True
        self.card.flip()
        self.assertFalse(self.card.is_open)

    def test_mouse_over_(self):
        mouse_position_x = 10
        mouse_position_y = 10
        result = self.card.card_chosen(mouse_position_x, mouse_position_y)
        self.assertTrue(result)

    def test_mouse_not_over(self):
        mouse_position_x = 100
        mouse_position_y = 100
        result = self.card.card_chosen(mouse_position_x, mouse_position_y)
        self.assertFalse(result)

    def test_cards_match(self):
        card1 = self.card
        card2 = self.card
        result = card1.is_matching(card2)
        self.assertTrue(result)
    
    def test_cards_not_matching(self):
        card1 = self.card
        card2 = Card(back_image_path, image_path, 0, 0)
        result = card1.is_matching(card2)
        self.assertFalse(result)
