#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from module_12.runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        r = Runner("Walk test")
        for x in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        r = Runner("Run test")
        for x in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        r1 = Runner("Walk test")
        r2 = Runner("Run test")
        for x in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == "__main__":
    unittest.main()
