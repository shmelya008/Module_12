import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r_1 = Runner('Serge')
        for i in range(10):
            r_1.walk()
            return r_1.distance
        self.assertEqual(r_1.distance, 50)

    #
    # def test_run(self):
    #     pass
    #
    # def test_challenge(self):
    #     pass

