import json
from datetime import datetime
from typing import List


class Question:

    def __init__(self, text: str, answers: List[str], right_answer: str):
        self.text = text
        self.answers = answers
        self.right_answer = right_answer

    @staticmethod
    def format_answer(user_answer: str) -> str:
        """Formatting given string"""
        return user_answer.lower().strip().replace(" ", "")

    @staticmethod
    def check_answer(user_answer: str, right_answer: str) -> bool:
        """Checking whether user's answer is correct or not"""
        return Question.format_answer(user_answer) == Question.format_answer(right_answer)

    def __str__(self):
        output = f"{self.text}\n"
        for answer in self.answers:
            output += f"-- {answer}\n"
        return output


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class QuestionLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_questions(self) -> List[Question]:
        """Loading list of questions in json file"""
        with open(self.file_path, encoding="UTF-8") as file:
            questions = json.load(file)
            return [
                Question(
                    text=question["question"],
                    answers=question["answers"],
                    right_answer=question["right_answer"]
                )
                for question in questions
            ]


class ScoreWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_score(self, player: Player, score: str):
        try:
            with open(self.file_path, "a") as file:
                file.write(f"Date: {datetime.now().date()}\n"
                           f"Player: {player}\n"
                           f"Score: {score}\n"
                           f"\n")
        except FileNotFoundError as error:
            print(f"Error writing score: {error}")


class Game:
    def __init__(self, question_loader: QuestionLoader, score_writer: ScoreWriter):
        self.score_writer = score_writer
        self.question_loader = question_loader

    @staticmethod
    def format_answer(user_answer):
        """Formatting given string"""
        return user_answer.lower().strip().replace(" ", "")

    def play(self):
        questions = self.question_loader.load_questions()
        correct_answer_counter = 0
        for question in questions:
            print(question)
            answer = input("Your answer: ")
            if question.check_answer(answer, question.right_answer):
                correct_answer_counter += 1
        name = input("You've answered all questions, but one. What's your name? ").capitalize().replace(' ', '')
        player = Player(name)
        score = f"{correct_answer_counter}/{len(questions)}"
        print(f"Thanks {player}! Your score is {score} :)")
        self.score_writer.write_score(player=player, score=score)


if __name__ == "__main__":
    question_loader = QuestionLoader(file_path="questions.json")
    score_writer = ScoreWriter(file_path="scores_obj.txt")
    game = Game(question_loader=question_loader, score_writer=score_writer)
    game.play()

