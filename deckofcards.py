class Card:
    def __init__(self, value):
        self.value = (value % 13) + 1
        suitValue = value - 52 * (value // 52) if value > 52 else value
        self.suit = (0 if suitValue < 52 / 4 else 1 if suitValue < 52 * 2 / 4
                     else 2 if suitValue < 52 * 3 / 4 else 3)
        return
    
    def __repr__(self):
        return ('A %s of %s' % (self.getCardType(), self.getSuit()))

    def getSuit(self):
        suit = 'Spades'
        if self.suit == 1:  suit = 'Hearts'
        elif self.suit == 2:    suit = 'Clubs'
        elif self.suit == 3:    suit = 'Diamonds'
        return suit

    def getCardType(self):
        card = ''
        if self.value == 1: card = 'Ace'
        elif self.value == 11:  card = 'Jack'
        elif self.value == 12:  card = 'Queen'
        elif self.value == 13:  card = 'King'
        else:   card = str(self.value)
        return card

class Deck:
    def __init__(self, numDecks=1):
        self.cards = []
        self.numDecks = numDecks
        self.deckLength = 52 * numDecks
        for i in range(self.deckLength):
            self.cards.append(Card(i))
        return

    def __repr__(self):
        return ('%i %i card deck[s]'
                % (self.numDecks, (self.deckLength / self.numDecks)))

    def showDeck(self):
        for card in self.cards:
            print(card)

myDeck = Deck()

from random import randint
def shuffleDeck(deck=myDeck, shuffles=1):
    for x in range(shuffles):
        for i in range(len(deck.cards) - 1):
            j = randint(i, len(deck.cards) - 1)
            deck.cards[i], deck.cards[j] = deck.cards[j], deck.cards[i]
    #print('That deck has been shuffled %i times' % shuffles)
