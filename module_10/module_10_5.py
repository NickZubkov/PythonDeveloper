#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = time.time()

    for name in filenames:
        read_info(name)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения линейное: {execution_time:.3f} секунд")

    start_time = time.time()
    with Pool() as p:
        p.map(read_info, filenames)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения многопроцессное: {execution_time:.3f} секунд")
