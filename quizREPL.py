"""
A CLI quiz application using a quiz module.

"""

import random

from quiz import Quiz
import sys
from html import unescape

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} quizname")

    score = 0
    for quiz_name in sys.argv[1:]:
        quiz = Quiz(quiz_name)
        quiz.load();
        for (i_item, item) in enumerate(quiz):

            print(f"Question {i_item +1} of {len(quiz)}")

            choice = 0
            correct_choice = -1
            while not choice:
                print(unescape(item.question))
                choices = list(item)
                random.shuffle(choices)
                for (i_ans, ans) in enumerate(choices):
                    if ans == item.correct_answer:
                        correct_choice = i_ans+1
                    print(f"     {i_ans +1}. {unescape(ans)}")
                try:
                    result = input("Type the number of your selection and press the enter key: ")
                    choice = int(result)
                    if choice < 1 or choice > len(item):
                        raise ValueError("invalid user input")
                except ValueError:
                    print(f"Invalid input. Your selection should be between 1 and {len(item)}. Try again.\n")
                    choice = 0

            if choice == correct_choice:
                print("Correct\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {unescape(item.correct_answer)}\n")

        print(f"Your total was {score} out of {len(quiz)}")


