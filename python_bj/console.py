import time
from itertools import repeat

class Console:
    def __init__(self, players):
        self.players = players

    def message(self, text):
        time.sleep(1)
        print(text)

    def info(self, text):
        def line(name = ''):
            return name + ''.join(repeat('-', 64 - len(name)))

        time.sleep(1)
        print(text)
        for player in self.players:
            print(line(player.name))
            print('hand: ' + ','.join(map(lambda card: card.info, player.hand)))
            print('score: ' + str(player.score))
            print(line())
