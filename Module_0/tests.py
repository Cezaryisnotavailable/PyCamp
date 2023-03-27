from datetime import datetime
import json
from unittest.mock import patch

import pytest

from task_1_obj import Question, QuestionLoader, ScoreWriter, Player, Game


def test_my_function(tmp_path):
    # use tmp_path in my tests
    assert str(tmp_path).endswith("my_function0")


@pytest.fixture
def sample_questions(tmp_path):
    """Creates a sample questions file for testing"""
    questions = [
        {
            "question": "What is the capital of France?",
            "answers": ["Paris", "Rome", "Berlin"],
            "right_answer": "Paris"
        },
        {
            "question": "What is the largest mammal in the world?",
            "answers": ["Elephant", "Blue Whale", "Giraffe"],
            "right_answer": "Blue Whale"
        }
    ]
    file_path = tmp_path / "questions.json"
    file_path.write_text(json.dumps(questions))
    return file_path


@pytest.fixture
def sample_scores_file(tmp_path):
    """Creates a sample scores file for testing"""
    file_path = tmp_path / "scores.txt"
    file_path.touch()
    return file_path


def test_questions():
    """Test to verify the Question class functionality"""
    question = Question(
        text="What is the capital of France?",
        answers=["Paris", "Rome", "Berlin"],
        right_answer="Paris"
    )
    assert question.text == "What is the capital of France?"
    assert question.answers == ["Paris", "Rome", "Berlin"]
    assert question.right_answer == "Paris"
    assert question.check_answer("Paris", "Paris") is True
    assert question.check_answer("paris", "Paris") is True
    assert question.check_answer("p  a ris", "Paris") is True
    assert not question.check_answer("rome", "Paris")


def test_question_loader(sample_questions):
    """Test to verify the QuestionLoader class functionality"""
    question_loader = QuestionLoader(file_path=sample_questions)
    questions = question_loader.load_questions()
    assert len(questions) == 2
    assert questions[0].text == "What is the capital of France?"
    assert questions[1].text == "What is the largest mammal in the world?"


def test_score_writer(sample_scores_file):
    """Test to verify the ScoreWriter class functionality"""
    score_writer = ScoreWriter(file_path=sample_scores_file)
    player = Player(name="Mario")
    score_writer.write_score(player=player, score="2/3")
    assert (
            sample_scores_file.read_text()
            == "Date: {}\nPlayer: Mario\nScore: 2/3\n\n".format(datetime.now().date())
    )


def test_game(sample_questions, sample_scores_file):
    """Test to verify the Game class functionality"""
    with patch("builtins.input", side_effect=["Paris", "Blue Whale", "Mario"]):
        question_loader = QuestionLoader(file_path=sample_questions)
        score_writer = ScoreWriter(file_path=sample_scores_file)
        game = Game(question_loader=question_loader, score_writer=score_writer)
        game.play()
    assert (
            sample_scores_file.read_text()
            == "Date: {}\nPlayer: Mario\nScore: 2/2\n\n".format(datetime.now().date())
    )
