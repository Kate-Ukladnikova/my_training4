# "Очереди для обмена данными между потоками"

import time
from queue import Queue
from random import randint
from threading import Thread

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(randint(3,10))
class Cafe:
    def __init__(self, tables, *quests):
        self.queue = Queue()
        self.tables = tables
        self.quests = quests
    def guest_arrival(self,*par_guests):
        global tr1
        counter_tables = 0
        for par_guest in par_guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = par_guest
                    tr1 = Thread(target=par_guest.run)
                    tr1.start()
                    print(f'{table.guest.name} ceл(а) за стол номер {table.number}')
                    tr1.join()
                    counter_tables += 1
                    break
                elif counter_tables == len(self.tables):
                    self.queue.put(par_guest)
                    print(f'{par_guest.name} в очереди')
                    break
                else:
                    continue
    def discuss_guests(self):
        global tr2
        global tr3
        if (self.queue is not Queue.empty) or self.is_table_busy:
            j = 0
            for table in self.tables:
                if tr1.is_alive and table.guest is not None:
                    j += 1
                    print(f'{table.guest.name} покушала(-а) и ушел(-а)\nCтол номер {table.number} свободен')
                    table.guest = None
                if (self.queue is not Queue.empty) and self.is_table_not_busy:
                    table.guest = self.queue.get(table)
                    print(f'{table.guest.name} вышел(-шла) из очереди и села за стол номер {table.number}')
                    tr2 = Thread(target=table.guest.run)
                    tr2.start()
                    tr2.join()
                if tr2.is_alive and table.guest is not None:
                    j += 1
                    print(f'{table.guest.name} покушала(-а) и ушел(-а)\nCтол номер {table.number} свободен')
                    table.guest = None
            for table in self.tables:
                if (self.queue is not Queue.empty) and self.is_table_not_busy:
                    table.guest = self.queue.get(table)
                    print(f'{table.guest.name} вышел(-шла) из очереди и села за стол номер {table.number}')
                    tr3 = Thread(target=table.guest.run)
                    tr3.start()
                    tr3.join()
                if tr3.is_alive and table.guest is not None:
                    j += 1
                    print(f'{table.guest.name} покушала(-а) и ушел(-а)\nCтол номер {table.number} свободен')
                    table.guest = None
                    if j >= len(self.quests):
                        break
    def is_table_busy(self):
        is_any_table_busy = False
        for table in self.tables:
            if table.guest is not None:
                is_any_table_busy = True
                break
        return is_any_table_busy
    def is_table_not_busy(self):
        is_any_table_not_busy = False
        for table in self.tables:
            if table.guest is None:
                is_any_table_not_busy = True
                break
        return is_any_table_not_busy

# Cоздание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Cоздание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(tables, *guests)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()