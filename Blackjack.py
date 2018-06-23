import random

playing = True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        for item in self.deck:
            print (item)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1
    def adjust_for_ace(self):
        while self.aces>0 and self.value>21:
            self.value-=10
            self.aces-=1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to bet?'))
        except:
            print('Please enter an integer')
        else:
            if chips.bet > chips.total:
                print(f'Bet exceeds balance, you have {chips.total} chips available, please enter a new bet')
            else:
                print(f'You have placed a bet of ${chips.bet}')
                break

def hit(deck,hand):
    random_card = deck.deal()
    hand.add_card(random_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while playing:
        decision = input('Would you like to hit or stand? Please enter h or s.')
        if decision == 'h':
            hit(deck,hand)
        elif decision == 's':
            print('Player stands, turn for the dealer')
            playing = False
        else:
            print('Sorry, not a valid entry. Please enter h or s')
        break

def show_some(player_hand,dealer_hand):
    print('Dealer Cards')
    print(dealer_hand.cards[1])
    print('Player Cards')
    for card in player_hand.cards:
        print(card)

def show_all(player_hand,dealer_hand):
    print('Player Cards')
    for card in player_hand.cards:
        print(card)
    print('Dealer Cards')
    for card in dealer_hand.cards:
        print(card)

def player_busts(player_hand,chips):
    print('Player busts, bet lost')
    chips.lose_bet()

def player_wins(player_hand,chips):
    print('Player wins this round!')
    chips.win_bet()

def dealer_busts(dealer_hand):
    print('Dealer busts, Player wins this round!')
    chips.win_bet()

def dealer_wins(dealer_hand):
    print('Player busts, bet lost')
    chips.lose_bet()

def push(player_hand,dealer_hand,chips):
    print('Its a tie, bet returned to your stack')

while True:
    print('Welcome to BLACKJACK!!!')
    chips = Chips()
    #Setup deck
    shuffled_deck = Deck()
    shuffled_deck.shuffle()
    #setup player
    player_hand = Hand()
    player_hand.add_card(shuffled_deck.deal())
    player_hand.add_card(shuffled_deck.deal())
    #setup dealer
    dealer_hand = Hand()
    dealer_hand.add_card(shuffled_deck.deal())
    dealer_hand.add_card(shuffled_deck.deal())
    
    take_bet(chips)
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(shuffled_deck, player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(dealer_hand,chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(shuffled_deck,dealer_hand)
    
        show_all(player_hand,dealer_hand)
    
        #winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(dealer_hand)
        else:
            push(player_hand,dealer_hand,chips)

    print(f'You have {chips.total} chips')

    new_game = input('would you like to play another game?')
    if new_game[0].lower == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing')
        break