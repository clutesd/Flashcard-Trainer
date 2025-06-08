import argparse
import json
import random
from pathlib import Path


def load_flashcards(path: Path):
    """Load flashcards from a JSON file."""
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError("Flashcard file must contain a list of objects")
    cards = []
    for item in data:
        if not isinstance(item, dict) or 'question' not in item or 'answer' not in item:
            raise ValueError("Each flashcard must have 'question' and 'answer'")
        cards.append({'question': str(item['question']), 'answer': str(item['answer'])})
    return cards


def run_quiz(cards):
    """Run the flashcard quiz."""
    correct = 0
    for card in cards:
        print(f"Q: {card['question']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == card['answer'].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. Answer: {card['answer']}\n")
    print(f"You answered {correct}/{len(cards)} correctly.")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple flashcard trainer")
    parser.add_argument("file", type=Path, help="Path to JSON file with flashcards")
    parser.add_argument("--shuffle", action="store_true", help="Shuffle flashcards before starting")
    args = parser.parse_args(argv)

    cards = load_flashcards(args.file)
    if args.shuffle:
        random.shuffle(cards)
    run_quiz(cards)


if __name__ == "__main__":
    main()
