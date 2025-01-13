# Тема "Логирование". Цель: получить опыт использования простейшего
# логирования совместно с тестами.
# Задача "Логирование бегунов"

import unittest
import logging
from module_12_1_test_4 import RunnerTest
from module_12_2_test_4 import TournamentTest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(levelname)s / %(message)s")

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)