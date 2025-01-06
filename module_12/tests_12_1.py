#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import unittest
from module_12.runner_and_tournament import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        r = Runner("Walk test", -5)
        try:
            if r.speed < 0:
                raise Exception("Скорость не может быть отрицательной")
            for x in range(10):
                r.walk()
            logging.info("test_walk выполнен успешно")
        except Exception as e:
            logging.warning(e)
        finally:
            self.assertEqual(r.distance, 50)



    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        r = Runner(5)
        try:
            if not isinstance(r.name, str):
                raise Exception("Неверный тип данных для объекта Runner")
            for x in range(10):
                r.run()
            logging.info("test_run выполнен успешно")
        except Exception as e:
            logging.warning(e)
        finally:
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
