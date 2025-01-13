import unittest
import logging
from rt_with_exceptions import Runner, Tournament
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
    def setUp(self):
        self.name_beguna_0 = Runner('Усэйн', -10)
        self.name_beguna_1 = Runner('Андрей', 9)
        self.name_beguna_2 = Runner(1, 3)
    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f"{i}: {j}")
    def test_zabegs_1(self):
        try:
            tournament = Tournament(90,self.name_beguna_0, self.name_beguna_2)
            result = tournament.start()
            self.all_results['TestMetod 1'] = {k: str(v) for k,v in result.items()}
            self.assertTrue(result[max(result)] == 'Ник')
            logging.info('test_walk выполнен успешно')
            logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                                encoding='utf-8', format="%(levelname)s / %(message)s")
        except:
            if isinstance(self.name_beguna_0.__str__(), str):
                logging.warning("Неверная скорость для Runner.")
            else:
                logging.warning("Неверный тип данных для объекта Runner")