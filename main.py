from deck import Deck
from card import Card
from storage import save_deck, load_deck


def main():
    current_deck = None  # No deck loaded at start
    while True:
        print("\n=== Flashcard Study App ===")
        print("1. Create new deck")
        print("2. Add card to deck")
        print("3. Study deck")
        print("4. Save deck")
        print("5. Load deck")
        print("6. Exit")
        
        choice = input("Choose an option:   ")
        
        if choice =="1":
            name =input("Enter the name of the deck:    ")
            current_deck = Deck(name)
            print(f"Creation of Deck with name {name} sucessful!")
            
            
        elif choice == '2':
            if current_deck == None:
                print("No deck loaded, please load or create one")
            else:
                front = input("Enter the card's front:   ")
                back  = input("Enter the card's back:    ")
                card = Card(front,back)
                current_deck.add_card(card)
                print(f"Sucessfully added card to {current_deck.name}")
                
        elif choice == '3':
            if current_deck is None:
                print("No deck loaded. Create or load a deck first.")
            else:
                due_Cards = current_deck.get_due_Cards()
                if len(due_Cards) == 0:
                    print("No cards to go off of")
                else: 
                    print(f"{len(due_Cards)} to go off of")
                    for card in current_deck.get_due_Cards():
                        print(card.front)
                        UI = input("Would you like the answer? (Yes/No)")
                        if UI.upper()=="YES":
                            print(card.back)
                        dif = int(input("Rate the difficulty from 1-3 with 1 being difficult and 3 being EASY"))
                        card.update_schedule(dif)
                        print(f"Card Scheduled!")
        
        elif choice == "4":
            if current_deck is None:
                print("No deck to go off of")
            else:
                filename = input("Enter in the name of file:    ")
                save_deck(current_deck,filename)
                
        elif choice == '5':
            filename = input("Enter in your filename:   ")
            loaded_deck = load_deck(filename)
            if loaded_deck is not None:
                current_deck = loaded_deck
                print(f"✓ Deck '{current_deck.name}' loaded with {len(current_deck.cards)} cards")
        
        elif choice == "6":
            print("Alright then! We'll see you on your way out!")
            break
        else:
            print("Error! Invalid choice")
            
if __name__ == "__main__":
    main()