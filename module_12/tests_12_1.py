import unittest
from module_12.runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = Runner("Walk test")
        for x in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner("Run test")
        for x in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = Runner("Walk test")
        r2 = Runner("Run test")
        for x in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == "__main__":
    unittest.main()
