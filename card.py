from datetime import datetime, timedelta

class Card:
    """
    Represents a single flashcard with spaced repetition scheduling.
    """
    
    def __init__(self, front, back):
        """
        Initialize a flashcard.
        
        Args:
            front (str): Question or term
            back (str): Answer or definition
        """
        self.front = front
        self.back = back
        self.ease_factor = 2.5  # Used in spaced repetition algorithm
        self.interval = 1  # Days until next review
        self.repetitions = 0  # Number of successful reviews
        self.next_review = datetime.now()  # When to review next
    
    def __str__(self):
        """String representation of the card."""
        return f"Q: {self.front}\nA: {self.back}"
    
    def update_schedule(self, difficulty):
        """
        Update the card's review schedule based on difficulty.
        
        Args:
            difficulty (int): 1=Hard, 2=Medium, 3=Easy
        """
        # TODO: Implement spaced repetition algorithm
        # For now, just a placeholder
        if difficulty == 1:  # Hard
            self.interval = 1
        elif difficulty == 2:  # Medium
            self.interval = 3
        else:  # Easy
            self.interval = 7
        
        self.next_review = datetime.now() + timedelta(days=self.interval)
        self.repetitions += 1
        
# Quick test
if __name__ == "__main__":
    # Test creating a card
    card = Card("What is a list in Python?", "A mutable, ordered sequence")
    print(card)
    print(f"\nNext review: {card.next_review}")
    
    # Test updating schedule
    card.update_schedule(3)  # Mark as easy
    print(f"After marking easy, next review: {card.next_review}")