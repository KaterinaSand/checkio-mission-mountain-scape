"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint
from my_solution import mountain_scape


def test_formula1(height: int, nb_tops: int):
    return {
        'input': [(height + 2 * n, height) for n in range(nb_tops)],
        'answer': height ** 2 + (2 * height - 1) * (nb_tops - 1),
    }


def make_random_tests(num):
    random_tests = []
    for _ in range(num):
        tops = []
        for _ in range(randint(3, 50)):
            x, y = 0, 1
            while (x + y) % 2:
                x = randint(0, 100)
                y = randint(1, randint(10, 50))
            tops.append([x, y])

        random_tests.append({
            "input": tops,
            "answer": mountain_scape(tops)
        })
    return random_tests


TESTS = {
    "Extra": [test_formula1(h, n) for h, n in ((3, 10), (5, 15), (10, 30))],
    "Randoms": make_random_tests(10),
    "Basics": [
        {
            "input": [[1, 1], [4, 2], [7, 3]],
            "answer": 13,
        },
        {
            "input": [[0, 2], [5, 3], [7, 5]],
            "answer": 29,
        },
        {
            "input": [[1, 3], [5, 3], [5, 5], [8, 4]],
            "answer": 37,
        },
    ],
}
