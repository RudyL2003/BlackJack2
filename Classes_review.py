import random as rand


class PlayingCards:
    '''An attempt to show playing cards'''
    def __init__ (self,suit,rank,value):
        '''Initialize Name and age of attributes.'''
        self.suit = suit
        self.rank = rank
        self.value = value
        self.name = self.rank+' of '+self.suit

    def face_down(self):
        '''Simulate a face down command'''
        print("This card is now is face down.")

    def face_up(self):
        """Simulate streatching in response to a command."""
        print(f"{self.name} is now face up!")


class Deck:
    '''an attempt to make a deck of cards'''
    def __init__ (self):
        self.cards = []
        self.reset()
        self.numcards=len(self.cards)
 
    def draw(self):
        self.numcards = self.numcards-1
        return self.cards.pop()

    def shuffle(self):
        rand.shuffle(self.cards)
        
    def reset(self):
        card_suits=["spades","dimonds","clubs","hearts"]
        card_ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        card_values=[1,2,3,4,5,6,7,8,9,10,10,10,10]
        self.cards=[]
        for suit in card_suits:
            for rank,value in zip(card_ranks,card_values):
                self.cards.append( PlayingCards(suit,rank,value))


my_deck=Deck()

card=my_deck.draw()
card.face_up()


my_deck.shuffle()
card=my_deck.draw()
card.face_up()