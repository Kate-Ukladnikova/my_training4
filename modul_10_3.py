# Tемa "Блокировки и обработка ошибок"
# Надо своить блокировки потоков, используя объекты класса Lock и его методы.
# Задача "Банковские операции":

import threading
from random import randint
import time
lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0
    def deposit(self):
        lock.acquire()
        for rand in range(0,100):
            random_number = randint(50,500)
            self.balance += random_number
            if self.balance >= 500 and lock.locked():
                self.balance -= random_number
                lock.release()
                break
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
        time.sleep(0.001)
    def take(self):
        lock.acquire()
        for rand in range(0,100):
            random_number = randint(50,500)
            print(f'Запрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.release()
                break
bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
