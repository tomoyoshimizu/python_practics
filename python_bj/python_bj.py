from console import Console
from player import Player
from card import Deck, Card

from itertools import product

class Game:

    def __init__(self):
        cards = []
        suits = ["spades", "hearts", "diams", "clubs"]
        ranks = list(range(2, 10)) + ["J", "Q", "K", "A"]
        for suit, rank in product(suits, ranks):
            cards.append(Card(suit, rank))

        self.deck = Deck(cards)
        self.dealer = Player("DEALER")
        self.you = Player("YOU")
        self.console = Console([self.dealer, self.you])

    def start(self):
        self.console.message("Game start!")

        result = {"dealer": 0, "you": 0}
        self.deck.shuffle()
        self.dealer.draw(self.deck, 1, True)
        self.dealer.draw(self.deck, 1, False)
        self.you.draw(self.deck, 2, True)

        self.console.info("Dealer dealt cards.")

        if self.you.score == 21:
            self.console.message("YOU get natural 21!")
            result["you"] = 22
        else:
            is_continue = True
            while is_continue:
                command = input("Would you like to draw another card? [y(hit)/n(stand)]").lower()
                if command in ["y", "yes", "hit"]:
                    self.you.draw(self.deck, 1, True)
                    self.console.info("YOU draw card.")
                    if self.you.score == 21:
                        self.console.message("YOU get 21!")
                        result["you"] = 21
                        is_continue = False
                    elif self.you.score > 21:
                        self.console.message("YOU bust!")
                        result["you"] = -1
                        is_continue = False
                elif command in ["n", "no", "stand"]:
                    self.console.message("YOU stand.")
                    result["you"] = self.you.score
                    is_continue = False
                else:
                    self.console.message("Invalid command.")

        self.dealer.hole_card_open()
        self.console.info("Hole card open!")

        if self.dealer.score == 21:
            self.console.message("DEALER get natural 21!")
            result["dealer"] = 22
        else:
            is_continue = True
            while is_continue:
                if self.dealer.score < 17:
                    self.dealer.draw(self.deck, 1, True)
                    self.console.info("DEALER draw card.")
                    if self.dealer.score == 21:
                        self.console.message("DEALER get 21!")
                        result["dealer"] = 21
                        is_continue = False
                    elif self.dealer.score > 21:
                        self.console.message("DEALER bust!")
                        result["dealer"] = 0
                        is_continue = False
                else:
                    result["dealer"] = self.dealer.score
                    is_continue = False


        if result["dealer"] == result["you"]:
            self.console.message("Draw game.")
        elif result["dealer"] < result["you"]:
            self.console.message("YOU win!")
        else:
            self.console.message("YOU lose.")

new_game = Game()
new_game.start()
