# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды, filter, map, zip, enumerate, списочные выражения

# Семинар 2, задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)