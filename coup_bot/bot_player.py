class RandomBot:

    cards = []
    coins = 0
    opponents = []

    def __init__(self):
        pass

    def start(self, cards, coins, players):
        self.cards = cards
        self.coins = coins
        self.opponents = players

    def play(self, must_coup):
        return {'action': 0, 'target': 0}

    def tries_to_block(self, action, player):
        return {'attempt_block': False, 'card': 0}

    def challenge(self, action, player, card):
        return {'challenges': True}

    def lose_influence(self):
        return {'card': 0}

    def give_card_to_inquisitor(self, player):
        return {'card': 0}

    def show_card_to_inquisitor(self):
        return {'change_card': False}

    def choose_card_to_return(self, player, card):
        return {'card': 0}

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