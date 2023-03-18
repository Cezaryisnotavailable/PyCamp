import json
from _datetime import datetime


def load_json():
    """Loading json file"""
    with open("questions.json") as file:
        data_to_be_loaded = json.load(file)
    return data_to_be_loaded


def format_answer(given_answer):
    """Formatting given string"""
    return given_answer.lower().strip().replace(" ", "")


def quiz(given_data):
    """Printing questions, checking answers and saving score to .txt file"""
    print(f"Welcome!\n Please answer for each of {len(given_data)} questions\n")
    correct_answer_counter = 0
    for question in given_data:
        print(f"{question['question']}\n")
        for answer in question['answers']:
            print(f"-- {answer}")

        answer = input("Your answer: ")
        if format_answer(answer) == format_answer(question["right_answer"]):
            correct_answer_counter += 1

    name = input("You've answered all questions, but one. What's your name? ").capitalize().replace(' ','')
    score = f"{correct_answer_counter}/{len(given_data)}"
    print(f"Thanks {name}! Your score is {score} :)")
    with open("scores.txt", "a") as file:
        file.write(f"Date: {datetime.now().date()}\n"
                   f"Player: {name}\n"
                   f"Score: {score}\n"
                   f"\n")


if __name__ == "__main__":
    data = load_json()
    quiz(data)
