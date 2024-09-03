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
        self.assertEqual(r_1.distance, 50)

    def test_run(self):
        r_2 = Runner('Alex')
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    def test_challenge(self):
        r_1 = Runner('Serge')
        r_2 = Runner('Alex')
        for i in range(10):
            r_1.walk()
            r_2.run()
            self.assertNotEqual(r_1.distance, r_2.distance)

