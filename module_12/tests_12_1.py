#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import unittest
from module_12.rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        try:
            r = Runner("Walk test", -5)
            for x in range(10):
                r.walk()
            logging.info("test_walk выполнен успешно")
            self.assertEqual(r.distance, 50)
        except ValueError as e:
            logging.warning(e)
            self.fail(e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        try:
            r = Runner(5)
            for x in range(10):
                r.run()
            logging.info("test_run выполнен успешно")
            self.assertEqual(r.distance, 100)
        except TypeError as e:
            logging.warning(e)
            self.fail(e)

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
