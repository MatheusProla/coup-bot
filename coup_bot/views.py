from django.http import HttpResponse, Http404
from bot_player import RandomBot

bot_player = RandomBot()

import json


def __decode_data(request):
    if request.method == 'POST':
        return json.loads(request.body)
    else:
        raise Http404


def __encode_data(response):
    return json.dumps(response)

'''
    cards: list
    coins: integer,
    players: list
'''
def start(request):
    data = __decode_data(request)
    cards = data['cards']
    coins = data['coins']
    players = data['players']
    bot_player.start(cards, coins, players)
    return HttpResponse()

'''
    must_coup: bool
'''
def play(request):
    data = __decode_data(request)
    must_coup = data['must_coup']
    response = bot_player.play(must_coup)
    return HttpResponse(__encode_data(response))

'''
    action: int
    player: string
'''
def tries_to_block(request):
    data = __decode_data(request)
    action = data['action']
    player = data['opponent']
    response = bot_player.tries_to_block(action, player)
    return HttpResponse(__encode_data(response))

'''
    action: int
    player: string
    card: string
'''
def challenge(request):
    data = __decode_data(request)
    action = data['action']
    player = data['opponent']
    card = data['card']
    response = bot_player.challenge(action, player, card)
    return HttpResponse(__encode_data(response))

'''
'''
def lose_influence(request):
    bot_player.lose_influence()
    return HttpResponse()

'''
    player: string
    card: string
'''
def inquisitor(request, action):
    data = __decode_data(request)
    if action == 'give_card_to_inquisitor':
        player = data['player']
        response = bot_player.give_card_to_inquisitor(player)
    elif action =='show_card_to_inquisitor':
        player = data['player']
        card = data['card']
        response = bot_player.show_card_to_inquisitor(player, card)
    elif action == 'choose_card_to_return':
        card = data['card']
        response = bot_player.choose_card_to_return(card)
    else:
        raise Http404
    return HttpResponse(__encode_data(response))

'''
    players: list
    player_acting: string,
    action": int
    player_blocking: string,
    challenger: int,
    challenged: int,
    card: string
'''
def status(request, action):
    data = __decode_data(request)
    if action == 'status':
        players = data['players']
        bot_player.signal_status(players)
    elif action == 'new_turn':
        player = data['opponent']
        bot_player.signal_new_turn(player)
    elif action == 'blocking':
        player_acting = data['player_acting']
        action = data['action']
        player = data['opponent']
        card = data['card']
        bot_player.signal_blocking(player_acting, action, player, card)
    elif action == 'lost_influence':
        player = data['player']
        card = data['card']
        bot_player.signal_lost_influence(player, card)
    elif action == 'challenge':
        challenger = data['challenger']
        challenged = data['challenged']
        card = data['card']
        bot_player.signal_challenge(challenger, challenged, card)
    elif action == 'action':
        player = data['opponent']
        action = data['action']
        player_targetted = data['player_targetted']
        bot_player.signal_action(player, action, player_targetted)
    else:
        raise Http404
    return HttpResponse()
