# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых
# слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с
# прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time
# import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков

# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время

# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время

from threading import Thread
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def timing(func):

    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        set_time = round(end_time - start_time, 2)
        print(f'Работа потоков: {set_time} секунд(Ы)')

    return wrapper


@timing
def first_words():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')


@timing
def second_words():
    thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
    thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
    thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
    thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

    thr_1.start()
    thr_2.start()
    thr_3.start()
    thr_4.start()

    thr_1.join()
    thr_2.join()
    thr_3.join()
    thr_4.join()


first_words()
second_words()
