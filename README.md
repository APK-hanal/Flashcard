Flashcard Study App(Started on Valentine's day 2026)

A command-line flashcard application with spaced repetition for effective studying.

Features
- Create custom flashcard decks
- Add cards with questions and answers
- Spaced repetition algorithm (cards reviewed at increasing intervals)
- Save/load decks to JSON files
- Track review progress

Installation

1. Clone this repo:
bash
git clone https://github.com/APK-hanal/Flashcard.git
cd Flashcard


2. Run the app:
bash
python main.py


Usage

Main Menu
1. **Create new deck** - Start a new flashcard deck
2. **Add card to deck** - Add question/answer pairs
3. **Study deck** - Review cards that are due
4. **Save deck** - Save to JSON file
5. **Load deck** - Load previously saved deck
6. **Exit** - Quit the app

Spaced Repetition
When studying, rate each card:
- **1 (Hard)** - Review again in 1 day
- **2 (Medium)** - Review again in 3 days
- **3 (Easy)** - Review again in 7 days

Cards you know well appear less frequently over time.

 Example Workflow
1. Create deck: "Python Basics"
2. Add cards:
   - "What is a list?" → "A mutable sequence"
   - "What is a tuple?" → "An immutable sequence"
3. Study the cards
4. Save as "python_basics"
5. Come back tomorrow, load "python_basics", study again


What I Learned

This was my first object-oriented programming project. I learned:
- Classes and objects in Python
- File I/O and JSON serialization
- DateTime manipulation
- Building a complete CLI application
- Git and GitHub workflow

Future Improvements
- [] Edit/delete cards
- [] Statistics (cards mastered, study streaks)
- [] Import cards from CSV
- [] Multiple difficulty levels
- [] GUI version
