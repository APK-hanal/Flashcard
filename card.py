from datetime import datetime



class Card:
    def __init__(self,front,back):
        self.front = front
        self.back =back
        self.next_review = datetime.now()
        self.interval = 1 
        self.repetitions = 0
    def __str__(self):
            return f"Question > {self.front} \nAnswer   > {self.back}"
        
            
        
if __name__ == "__main__":
    card = Card("What is Python?", "A programming language")
    print(card)