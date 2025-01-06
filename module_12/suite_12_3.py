import unittest
from module_12.tests_12_1 import RunnerTest
from module_12.tests_12_2 import TournamentTest

module_12_Tests = unittest.TestSuite()

module_12_Tests.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
module_12_Tests.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(module_12_Tests)
