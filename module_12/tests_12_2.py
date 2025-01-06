#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from module_12.runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_race1(self):
        t = Tournament(90, self.runner1, self.runner3)
        self.all_results[0] = t.start()
        unittest.TestCase.assertTrue(self.all_results[0][1], "Ник")

    def test_race2(self):
        t = Tournament(90, self.runner2, self.runner3)
        self.all_results[1] = t.start()
        unittest.TestCase.assertTrue(self.all_results[1][1], "Ник")

    def test_race3(self):
        t = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[2] = t.start()
        unittest.TestCase.assertTrue(self.all_results[2][2], "Ник")


    @classmethod
    def tearDownClass(cls):
        for race, results in cls.all_results.items():
            formatted_results = ", ".join(f"{key}: {value}" for key, value in results.items())
            print(f"{{{formatted_results}}}")

if __name__ == "__main__":
    unittest.main()