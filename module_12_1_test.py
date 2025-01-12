import unittest
import module_12_1

class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r = module_12_1.Runner('')
        for _ in range(0,10):
            var = r.walk()
        self.assertEqual(var, 50)
    def test_run(self):
        r2 = module_12_1.Runner('')
        for _ in range(0, 10):
            var2 = r2.run()
        self.assertEqual(var2, 100)
    def test_challenge(self):
        r3 = module_12_1.Runner('')
        r4 = module_12_1.Runner('')
        for _ in range(0, 10):
            var3 = r3.run()
            var4 = r4.walk()
        self.assertNotEqual(var3, var4)
