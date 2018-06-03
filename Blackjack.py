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
        pass

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.card = card
        self.cards.append(self.card)
        self.value += values[self.card.rank]
        if self.card.rank == 'Ace':
            self.aces+=1
    def adjust_for_ace(self):
        if self.aces>0 and self.value>21:
            self.value-=10

test_deck = Deck()
print(test_deck)
