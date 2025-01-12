# Tема "Систематизация и пропуск тестов".
# Цель: понять на практике как объединять тесты при помощи TestSuite.
# Научиться пропускать тесты при помощи встроенных в unittest декораторов.
# Задача "Заморозка кейсов"

import unittest

# Часть 1. TestSuit. Чтобы тесты сработали без заморозки раскомментируйте 4 последних
# оператора в блоке (16-19 строчки).

from module_12_1_test import RunnerTest
from module_12_2_test import TournamentTest
import suite_12_3
tmp = suite_12_3
ts = unittest.TestSuite()
# ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
# ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(ts)

# Часть 2. Пропуск тестов.

ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)