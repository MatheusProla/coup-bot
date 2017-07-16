from constants import *
from random import randint


class RandomBot:

    cards = []
    coins = 0
    opponents = {}

    def __init__(self):
        pass

    def start(self, cards, coins, players):
        self.cards = cards
        self.coins = coins
        for player in players:
            self.opponents[player] = {'coins': 2}
        print self.cards
        print self.coins
        print self.opponents

    def play(self, must_coup):
        sorted(self.opponents.items(), key=lambda x: x[1]['coins'], reverse=True)
        print self.opponents
        if (must_coup or (self.coins >= 7 and randint(0, 2) == 1)):
            return {'action': COUP}
        else:
            if DUKE in self.cards:
                return {'action': COLLECT_TAXES}
            elif CAPTAIN in self.cards and randint(0, 3) > 2:
                return {'action': EXTORTION, 'target': self.opponents.keys()[0]}
            elif ASSASSIN in self.cards and self.coins >= 3:
                return {'action': ASSASSIN, 'target': self.opponents.keys()[0]}
            elif randint(0, 3) == 1:
                return {'action': FOREIGN_AID}
            elif randint(0, 5) == 1:
                return {'action': EXCHANGE}
            elif randint(0, 4) == 1:
                return {'action': INVESTIGATE, 'target': self.opponents.keys()[0]}
            else:
                return {'action': INCOME}

    def tries_to_block(self, action, player):
        if action == EXTORTION:
            if CAPTAIN in self.cards:
                return {'attempt_block': True, 'card': CAPTAIN}
            elif INQUISITOR in self.cards:
                return {'attempt_block': True, 'card': INQUISITOR}
        elif FOREIGN_AID:
            if DUKE in self.cards or randint(0, 5) == 1:
                return {'attempt_block': True, 'card': DUKE}
        elif ASSASSINATE:
            if CONTESSA in self.cards:
                return {'attempt_block': True, 'card': CONTESSA}
        return {'attempt_block': False}

    def challenge(self, action, player, card):
        if (card == DUKE and randint(0, 1) == 0):
            return {'challenges': True}
        else:
            return {'challenges': False}

    def lose_influence(self):
        return {'card': self.cards[0]}

    def give_card_to_inquisitor(self, player):
        return {'card': self.cards[0]}

    def show_card_to_inquisitor(self):
        return {'change_card': True}

    def choose_card_to_return(self, player, card):
        return {'card': self.cards[0]}

    def signal_status(self, players):
        pass

    def signal_new_turn(self, player):
        pass

    def signal_blocking(self, player_acting, action, player_blocking, card):
        pass

    def signal_lost_influence(self, player, card):
        pass

    def signal_challenge(self, challenger, challenged, card):
        pass

    def signal_action(self, player, action, player_targetted):
        pass
