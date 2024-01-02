questions = [
    "What is the sum of all even numbers from 2 to 20?",
    "Which is the only prime number that is even?",
    # ... more questions
]

answers = [
    ["70", "110", "120", "140"],
    ["2", "4", "6", "8"],
    # ... corresponding answer lists
]

correct_answers = [1, 0, ...]  # Indices of correct answers in `answers` list
question_bank = [
    ["What is the sum of all even numbers from 2 to 20?", ["70", "110", "120", "140"], "110"],
    ["Which is the only prime number that is even?", ["2", "4", "6", "8"], "0"],
    # ... more question sets
]
question_bank = [
    {
        "question": "What is the sum of all even numbers from 2 to 20?",
        "answers": ["70", "110", "120", "140"],
        "correct_answer": "110"
    },
    {
        "question": "Which is the only prime number that is even?",
        "answers": ["2", "4", "6", "8"],
        "correct_answer": "2"
    },
    # ... more questions
]
class Question:
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

    # ... methods for displaying, checking answers, etc.
