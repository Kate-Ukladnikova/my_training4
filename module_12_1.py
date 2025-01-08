# "Простые Юнит-Тесты"
# Цель: приобрести навык создания простейших Юнит-тестов
# Задача "Проверка на выносливость"

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        return self.distance

    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name