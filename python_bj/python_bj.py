from console import Console
from player import Player
from card import Deck, Card

from itertools import product

class Game:
    def __init__(self):
        suits = ['spades', 'hearts', 'diams', 'clubs']
        ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
        self.deck = Deck([Card(*card) for card in product(suits, ranks)])
        self.dealer = Player('DEALER')
        self.you = Player('YOU')
        self.console = Console([self.dealer, self.you])

    def start(self):
        bet = 0
        while True:
            command = int(input('Place your Bet. [YOU have ' + str(self.you.chip) + ' chips.]: '))
            if self.you.chip >= command > 0:
                bet = command
                self.you.chip -= bet
                break
            elif self.you.chip < command:
                self.console.message('Lack of chips.')
            else:
                self.console.message('Invalid command.')

        self.console.message('Game start!')

        result = {'dealer': 0, 'you': 0}
        self.deck.shuffle()
        self.dealer.draw(self.deck, 1, True)
        self.dealer.draw(self.deck, 1, False)
        self.you.draw(self.deck, 2, True)

        self.console.info('DEALER dealt cards.')

        if self.you.score == 21:
            self.console.message('YOU get natural 21!')
            result['you'] = 22
        else:
            while True:
                command = input('Would you like to draw another card? [y(hit)/n(stand)]: ').lower()
                if command in ['y', 'yes', 'hit']:
                    self.you.draw(self.deck, 1, True)
                    self.console.info('YOU draw card.')
                    if self.you.score == 21:
                        self.console.message('YOU get 21!')
                        result['you'] = 21
                        break
                    elif self.you.score > 21:
                        self.console.message('YOU bust!')
                        result['you'] = -1
                        break
                elif command in ['n', 'no', 'stand']:
                    self.console.message('YOU stand.')
                    result['you'] = self.you.score
                    break
                else:
                    self.console.message('Invalid command.')

        self.dealer.hole_card_open()
        self.console.info('Hole card open!')

        if self.dealer.score == 21:
            self.console.message('DEALER get natural 21!')
            result['dealer'] = 22
        else:
            while True:
                if self.dealer.score < 17:
                    self.dealer.draw(self.deck, 1, True)
                    self.console.info('DEALER draw card.')
                    if self.dealer.score == 21:
                        self.console.message('DEALER get 21!')
                        result['dealer'] = 21
                        break
                    elif self.dealer.score > 21:
                        self.console.message('DEALER bust!')
                        result['dealer'] = 0
                        break
                else:
                    result['dealer'] = self.dealer.score
                    break

        if result['dealer'] == result['you']:
            self.console.message('Draw game.')
            self.you.chip += bet
        elif result['dealer'] < result['you']:
            self.console.message('YOU win!')
            if result['you'] >= 21:
                self.you.chip += round(bet * 2.5)
            else:
                self.you.chip += bet * 2
        else:
            self.console.message('YOU lose.')

        print('[YOU have ' + str(self.you.chip) + 'chips.]')
        self.dealer.return_cards(self.deck)
        self.you.return_cards(self.deck)


game = Game()
while True:
    game.start()
    if game.you.chip == 0:
        print('Your chips are gone')
        break
    command = input('Do you want to continue playing the game? [Y/n]: ').lower()
    if command in ['n', 'no', 'stand']:
        break
