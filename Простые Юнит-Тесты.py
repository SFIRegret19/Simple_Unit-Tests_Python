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
    # def __init__(self, methodName = "runTest"):
    #     super().__init__(methodName)

    def test_walk(self):
        runner = Runner('Гриша')

        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Гриша')

        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Гриша')
        runner2 = Runner('Петя')

        for _ in range(10):
            runner1.walk()

        for _ in range(10):
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()