from datetime import datetime,timedelta



class Card:
    def __init__(self,front,back):
        self.front = front
        self.back =back
        self.next_review = datetime.now()
        self.interval = 1 
        self.repetitions = 0
        
        
    def __str__(self):
            return f"Question > {self.front} \nAnswer   > {self.back}"
        
    def update_schedule(self, difficulty):
        if difficulty == 1:
            self.interval = 1
            self.next_review = datetime.now() + timedelta(days=1)
            self.repetitions +=1
        if difficulty == 2:
            self.interval = 3
            self.next_review = datetime.now() + timedelta(days=3)
            self.repetitions += 1
        if difficulty ==3:
            self.interval = 7
            self.next_review = datetime.now() + timedelta(days=7)
            self.repetitions +=1 
        
            
        
if __name__ == "__main__":
    card = Card("What is Python?", "A programming language")
    print(f"Initial next review: {card.next_review}")
    print(f"Initial repetitions: {card.repetitions}")
    
    # Mark as easy
    card.update_schedule(3)
    
    print(f"\nAfter marking EASY:")
    print(f"Next review: {card.next_review}")
    print(f"Interval: {card.interval} days")
    print(f"Repetitions: {card.repetitions}")