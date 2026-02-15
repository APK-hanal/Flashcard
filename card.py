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
        elif difficulty == 2:
            self.interval = 3
            self.next_review = datetime.now() + timedelta(days=3)
            self.repetitions += 1
        else:
            self.interval = 7
            self.next_review = datetime.now() + timedelta(days=7)
            self.repetitions +=1 
            
    def to_dict(self):
        #converts the card with all of the values as keys
        return {'front' : self.front,
                'back':self.back,
                'next_review' : self.next_review.isoformat(),
                'interval' : self.interval,
                'repetitions' : self.repetitions
                }
        
    @staticmethod
    def from_dict(data):
        card = Card(data['front'], data['back'])
        card.next_review = datetime.fromisoformat(data['next_review'])
        card.interval = data['interval']
        card.repetitions = data['repetitions']
        return card