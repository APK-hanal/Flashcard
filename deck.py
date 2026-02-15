from datetime import datetime,timedelta
from card import Card
class Deck:
    def __init__(self,name):
        self.name = name
        self.cards = []
        
    def add_card(self,card):
        self.cards.append(card)
        
    def get_due_Cards(self):
        time = datetime.now()
        due_cards = []
        for card in self.cards:
            if card.next_review <= time:
                due_cards.append(card)
        return due_cards
    
    def to_dict(self):
        #deck ----> dict
        card_dict= []
        for cards in self.cards:
            
            card_dict.append(cards.to_dict())
            
        return {'name':self.name,
                'cards': card_dict
                }
    @staticmethod
    def from_dict(data):
        deck = Deck(data['name'])
        card_obj = []
        for card_dict in data['cards']:
            card_obj.append(Card.from_dict(card_dict))
        deck.cards = card_obj
        return deck
            
        
        
            
            