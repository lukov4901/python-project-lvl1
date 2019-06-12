# -*- coding: utf-8 -*-

"""Brain even game functions."""

from brain_games.engine import generate_number


def make_question():
    """Generate game question."""
    number = generate_number()
    question = 'Question: {number}'.format(number=number)
    answer = correct_answer(number)
    return (question, answer)


def correct_answer(number):
    """Return expected answer."""
    return 'yes' if number % 2 == 0 else 'no'
