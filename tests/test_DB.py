from unittest import TestCase
from quiz import Quiz
from persist_json import load, store, destroy
import os


class TestDBOps(TestCase):

    def test_load_succeed(self):
        quiz = Quiz("q")
        quiz.add("question", "correct answer", ["incorrect1", "incorrect2", "incorrect3"])
        store(quiz)
        loaded_quiz = load(quiz)
        self.assertEquals(quiz, loaded_quiz)
        destroy("q")

    def test_load_error(self):
        quiz = Quiz("not_exist_quiz")
        self.assertRaises(IOError, quiz.load)

    def test_store_succeed(self):
        quiz = Quiz("q")
        quiz.add("question", "correct answer", ["incorrect1", "incorrect2", "incorrect3"])
        store(quiz)
        self.assertTrue(os.path.exists("data/q"))

    def test_store_error(self):
        quiz = Quiz("q")
        quiz.add("question", "correct answer", ["incorrect1", "incorrect2", "incorrect3"])
        store(quiz)
        self.assertRaises(IOError, quiz.load)

    def test_destroy_succeed(self):
        quiz = Quiz("q")
        quiz.add("question", "correct answer", ["incorrect1", "incorrect2", "incorrect3"])
        store(quiz)
        destroy("q")
        self.assertFalse(os.path.exists("data/q"))

    def test_destroy_error(self):
        quiz = Quiz("not_exist_quiz")
        self.assertRaises(IOError, quiz.destroy)

