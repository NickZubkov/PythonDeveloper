import logging
import unittest
from module_12.tests_12_1 import RunnerTest

module_12_Tests = unittest.TestSuite()

module_12_Tests.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                         format="%(asctime)s | %(levelname)s | %(message)s")
    runner.run(module_12_Tests)
