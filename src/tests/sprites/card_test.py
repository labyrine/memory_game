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

    def test_card_not_open_and_mouse_over_before_choosing(self):
        self.card.is_open = False
        mouse_position = (10, 10)
        self.card.card_chosen(mouse_position)
        self.assertTrue(self.card.is_open)

    def test_card_not_open_and_mouse_not_over_before_choosing(self):
        self.card.is_open = False
        mouse_position = (100, 100)
        self.card.card_chosen(mouse_position)
        self.assertFalse(self.card.is_open)

    def test_card_opened_and_mouse_not_over_before_choosing(self):
        self.card.is_open = True
        mouse_position = (100, 100)
        self.card.card_chosen(mouse_position)
        self.assertTrue(self.card.is_open)
