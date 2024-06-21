class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chip = 500

    @property
    def score(self):
        score = 0
        num_of_ace = 0
        for card in self.hand:
            if not card.is_open:
                continue
            elif card.rank == 'A':
                num_of_ace += 1
            elif card.rank in ['J', 'Q', 'K']:
                score += 10
            else:
                score += card.rank
        for _ in range(num_of_ace):
            score += 11 if score <= 10 else 1
        return score

    def draw(self, deck, num_of_cards, is_open):
        for _ in range(num_of_cards):
            if not deck.cards:
                print('There are no cards in the deck.')
                break
            else:
                draw_card = deck.cards[0]
                del deck.cards[0]
                draw_card.is_open = is_open
                self.hand.append(draw_card)

    def hole_card_open(self):
        for card in self.hand:
            card.is_open = True

    def return_cards(self, deck):
        for card in self.hand:
            deck.cards.append(card)
        self.hand.clear()
