import sys
import pygame


class GameLoop:
    def __init__(self, setup, renderer, event_queue, clock):
        self._setup = setup
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.all_cards = self._setup.all_cards
        self.pairs_count = len(self.all_cards) // 2
        self.points = 0
        self.cards_turned = []
        # Generated code starts
        self.flip_timer = self._clock.get_ticks()
        # Generated code ends

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._process_turned_cards()
            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for card in self.all_cards:
                    if card.card_chosen(mouse_x, mouse_y) and len(self.cards_turned) < 2 and card not in self.cards_turned:
                        card.flip()
                        self.cards_turned.append(card)
            elif event.type == pygame.QUIT:
                return False

    def _process_turned_cards(self):
        if len(self.cards_turned) == 2:
            current_time = self._clock.get_ticks()
            # Generated code starts
            if current_time - self.flip_timer > 3000:
                # Generated code ends
                if self.cards_turned[0].is_matching(self.cards_turned[1]):
                    self.points += 1
                    self.cards_turned[0].delete_found()
                    self.cards_turned[1].delete_found()
                    self.cards_turned = []
                    if self.points == self.pairs_count:
                        pygame.quit()
                        sys.exit()
                elif not self.cards_turned[0].is_matching(self.cards_turned[1]):
                    self.cards_turned[0].flip()
                    self.cards_turned[1].flip()
                    self.cards_turned = []
                # Generated code starts
                self.flip_timer = self._clock.get_ticks()
                # Generated code ends

    def _render(self):
        self._renderer.render()
