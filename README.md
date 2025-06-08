# Flashcard-Trainer

AI-Powered Flashcard App

This repository contains a simple command line flashcard trainer.

## Usage

1. Prepare a JSON file containing your flashcards. Each flashcard must have
   a `question` and an `answer` field.

Example (`sample_flashcards.json`):

```
[
    {"question": "Capital of France", "answer": "Paris"},
    {"question": "2 + 2", "answer": "4"},
    {"question": "Largest planet", "answer": "Jupiter"}
]
```

2. Run the trainer using Python:

```
python main.py sample_flashcards.json --shuffle
```

The program will prompt you with each question and let you know whether your
answer is correct.
