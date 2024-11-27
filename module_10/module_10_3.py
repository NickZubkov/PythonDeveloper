#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import random

class Bank:
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rnd = random.randint(50, 500)
            self.balance += rnd
            print(f'Пополнение: {rnd}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rnd = random.randint(50, 500)
            print(f'Запрос на {rnd}')
            if rnd <= self.balance:
                self.balance -= rnd
                print(f'Снятие: {rnd}. Баланс: {self.balance}')
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