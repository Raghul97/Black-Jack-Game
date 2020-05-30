"""
This module is created for blackjack game, played between a computer and player.
I hope u enjoy this game.

--Raghul R
"""
import random
from black import Account

print(" *** Welcome to BlackJack Game *** ")
print(" *** Single Player Mode *** ")

while True:
    start = input(" Press Enter key to start: ")
    if len(start) == 0:
        begin = True
        break
    else:
        begin = False

playerpopint = 0
computerpoint = 0


def player(card1, card2):
    global playerpoint
    point = 0
    print(f'player: {card1}')
    print(f'Computer: {card2}')
    count = 0
    while True:
        if 'A' in card1:
            pos = card1.index('A')
            card1.pop(pos)
            count += 1
            continue
        else:
            break
    while count != 0:
        card1.append('A')
        count -= 1
    for i in card1:
        if i in ['K', 'Q', 'J']:
            point += 10
        elif i in range(2, 11):
            point += i
        else:
            if i == 'A':
                if (point + 11) >= 21:
                    point += 1
                else:
                    point += 11
    playerpoint = point

    return check(point)


def check(pts):
    if pts < 21:
        return True
    else:
        return False


def hit(rem_cards, pla_card, computer_card):
    pla_card.append(rem_cards[-1])
    rem_cards.pop()
    scr = player(pla_card, computer_card)
    return scr


def computer(card1, card2):
    global computerpoint
    point = 0
    print(f'player: {card1}')
    print(f'Computer: {card2}')
    count = 0
    while True:
        if 'A' in card2:
            pos = card2.index('A')
            card2.pop(pos)
            count += 1
            continue
        else:
            break
    while count != 0:
        card2.append('A')
        count -= 1
    for i in card2:
        if i in ['K', 'Q', 'J']:
            point += 10
        elif i in range(2, 11):
            point += i
        else:
            if i == 'A':
                if (point + 11) >= 21:
                    point += 1
                else:
                    point += 11
    computerpoint = point
    return point


def compcheck(point):
    if 15 < point < 21:
        return False
    elif point <= 15:
        return True
    else:
        return False


def compuhit(rem_card, pla_card, computer_card):
    pots = computer(pla_card, computer_card)
    seri = check(pots)
    while seri:
        print(" Computer Hit's ")
        computer_card.append(rem_card[-1])
        rem_card.pop()
        pts = computer(pla_card, computer_card)
        zoom = compcheck(pts)
        if zoom:
            seri = True
        else:
            seri = check(pts)
            if seri:
                return True
    else:
        return False


while begin:
    print(' The Game Begins! ')
    while True:
        try:
            cash = int(input(" Enter the Total amount you need to deposit: "))
        except TypeError:
            print(" Enter a valid amount: ")
        else:
            break
    instant = Account()
    deposited = instant.deposit(cash)
    loop = True
    while loop:
        deck = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
        random.shuffle(deck)
        while True:
            n = 1
            playercard = []
            computercard = []
            alias = []
            while n < 5:
                if n % 2 != 0:
                    playercard.append(deck[-1])
                    deck.pop()
                else:
                    computercard.append(deck[-1])
                    alias.append(deck[-1])
                    deck.pop()
                n += 1
            break
        alias[0] = 'Hidden'
        okay = player(playercard, alias)
        while True:
            while okay:
                print(" Player Turn ")
                task = input(' Hit or Stay?? ( H or S ) ')
                if task.upper() == 'H':
                    okay = hit(deck, playercard, computercard)
                elif task.upper() == 'S':
                    comp = True
                    break
                else:
                    print(' Sorry!, I could not understand. ')
                    print(' Enter correct key words as mentioned. ')
            else:
                print(" player busts !!!! ")
                break
            while comp:
                okay = compuhit(deck, playercard, computercard)
                if okay:
                    break
                else:
                    comp = False
            else:
                print(' Computer busted ')
                break

        begin = False
        break


