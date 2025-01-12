# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase

import unittest
from runner_and_tournament import Runner, Tournament
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
    def setUp(self):
        self.name_beguna_0 = Runner('Усэйн', 10)
        self.name_beguna_1 = Runner('Андрей', 9)
        self.name_beguna_2 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f"{i}: {j}")
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_zabegs_1(self):
        tournament = Tournament(90,self.name_beguna_0, self.name_beguna_2)
        result = tournament.start()
        self.all_results['TestMetod 1'] = {k: str(v) for k,v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_zabegs_2(self):
        tournament = Tournament(90, self.name_beguna_1, self.name_beguna_2)
        result = tournament.start()
        self.all_results['TestMetod 2'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_zabegs_3(self):
        tournament = Tournament(90, self.name_beguna_1, self.name_beguna_0, self.name_beguna_2)
        result = tournament.start()
        self.all_results['TestMetod 3'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')