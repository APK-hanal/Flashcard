import json 
from deck import Deck


def save_deck(deck, filename):
    filepath = f"data/{filename}.json"
    deck_dict = deck.to_dict()
    with open(filepath, 'w') as f:
        json.dump(deck_dict,f,indent=2)
    
    print(f"Deck Sucessfully save to {filepath}")
    
def load_deck(filename):
    filepath = f'data/{filename}.json'
    try:
        with open(filepath, 'r') as f:
            deck_dict = json.load(f)
            deck_obj = Deck.from_dict(deck_dict)
            return deck_obj
    except FileNotFoundError:
        print("Error! file not found")
        return None
    