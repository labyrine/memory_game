import unittest
from services.memory_game_setup import MemoryGameSetUp
import os


class TestMemoryGameSetUp(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.src_path = os.path.abspath(
            os.path.join(self.current_directory, '..', '..'))
        self.game_setup = MemoryGameSetUp(self.src_path, 800, 600)

    def test_width_attribute(self):
        self.assertEqual(self.game_setup.width, 800)

    def test_height_attribute(self):
        self.assertEqual(self.game_setup.height, 600)

    def test_current_directory_attribute(self):
        self.assertEqual(self.game_setup.current_directory, self.src_path)

    def test_card_positions(self):
        for row in range(5):
            for col in range(8):
                index = row * 8 + col
                x_pos = 10 + col * (800 // 8)
                y_pos = 110 + row * ((600 - 100) // 5)

                card = self.game_setup.all_cards.sprites()[index]

                self.assertEqual(card.rect.x, x_pos)
                self.assertEqual(card.rect.y, y_pos)
