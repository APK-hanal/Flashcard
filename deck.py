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
    
if __name__ == "__main__":
    deck = Deck("Python Basics")
    
    # Add some cards
    card1 = Card("What is Python?", "A language")
    card2 = Card("What is a list?", "Mutable sequence")
    
    # Make card2 not due yet (future review)
    card2.next_review = datetime.now() + timedelta(days=5)
    
    deck.add_card(card1)
    deck.add_card(card2)
    
    print(f"Total cards: {len(deck.cards)}")
    print(f"Due cards: {len(deck.get_due_Cards())}")
        
            
            