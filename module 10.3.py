# Задача "Банковские операции":

import threading
import time
from random import randint

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for popolnenie in range(100):
            number = randint(50,500)
            self.balance = self.balance + number
            print(f"Пополнение: {number}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for snyatie in range(100):
            number2 = randint(50,500)
            print(f"Запрос на {number2}")
            if self.balance >= number2:
                self.balance = self.balance - number2
                print(f"Снятие: {number2}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
