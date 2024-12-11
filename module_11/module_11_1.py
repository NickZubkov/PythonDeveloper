#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

if response.status_code == 200:
    data = response.json()
    print("Данные успешно получены:", data)
else:
    print("Ошибка запроса:", response.status_code)

array = np.array([1, 2, 3, 4, 5])
squared_array = np.square(array)
mean_value = np.mean(array)
cumsum_array = np.cumsum(array)

print("Исходный массив:", array)
print("Квадраты элементов:", squared_array)
print("Среднее значение:", mean_value)
print("Накопительная сумма:", cumsum_array)

image = Image.new("RGB", (600, 400), color="white")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=16)

title = "Результаты вычислений:"
data_text = f"Исходный массив: {array}\nКвадраты: {squared_array}\nСреднее: {mean_value:.2f}\nНакопительная сумма: {cumsum_array}"

draw.text((20, 20), title, fill="black", font=font)
draw.text((20, 60), data_text, fill="black", font=font)

image.save("results.png")
print("Изображение сохранено как 'results.png'")

