#Homework4 task1
'''
Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання.
Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування
алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності 
алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання 
алгоритмів використовуйте модуль timeit.
'''

import timeit

# Функція сортування вставками
def insertion_sort(input_data):
    for i in range(1, len(input_data)):  # Починаємо з другого елемента масиву
        key = input_data[i]  # Зберігаємо поточний елемент як ключ
        j = i - 1  # Починаємо порівнювати з попереднім елементом
        while j >= 0 and key < input_data[j]:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
            input_data[j + 1] = input_data[j]  # Зсуваємо поточний елемент вправо
            j -= 1  # Переміщаємось на одну позицію вліво
        input_data[j + 1] = key  # Вставляємо ключ на правильну позицію
    return input_data  # Повертаємо відсортований масив


# Функція сортування злиттям
def merge_sort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є
    if len(arr) <= 1:
        return arr

    # Визначаємо середину масиву
    mid = len(arr) // 2
    # Ділимо масив на ліву і праву половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Зливаємо дві відсортовані половини
    return merge(left_half, right_half)


# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив

setup_code = '''
array_5 = [12, 11, 13, 5, 6, 7]
'''

setup_code2 = '''
array_20 = [12, 11, 13, 5, 6, 7,
            12, 11, 13, 5, 6, 7,
            12, 11, 13, 5, 6, 7,
            12, 11, 13, 5, 6, 7,
            12, 11, 13, 5, 6, 7]
'''
# Приклад використання
# Використання та замір Timsort з бібліотеки python 
test_code_sorted = '''
sorted_list = sorted(array_5)
'''
test_code_sorted2 = '''
sorted_list = sorted(array_20)
'''

execution_time = timeit.timeit(stmt=test_code_sorted, setup=setup_code, number=100000)
print(f"Execution time of sorted: {execution_time} seconds")
execution_time = timeit.timeit(stmt=test_code_sorted2, setup=setup_code2, number=100000)
print(f"Execution time of sorted 2: {execution_time} seconds")

# Використання та замір сортування вставками 
test_code_insertion = '''
from __main__ import insertion_sort
sorted_list = insertion_sort(array_5)
'''
test_code_insertion2 = '''
from __main__ import insertion_sort
sorted_list = insertion_sort(array_20)
'''

execution_time = timeit.timeit(stmt=test_code_insertion, setup=setup_code, number=100000)
print(f"Execution time of insertion sort: {execution_time} seconds")
execution_time = timeit.timeit(stmt=test_code_insertion2, setup=setup_code2, number=100000)
print(f"Execution time of insertion sort 2: {execution_time} seconds")

# Використання та замір сортування злиттям 
test_code_merge = '''
from __main__ import merge_sort, merge
sorted_list = merge_sort(array_5)
'''
test_code_merge2 = '''
from __main__ import merge_sort, merge
sorted_list = merge_sort(array_20)
'''
execution_time = timeit.timeit(stmt=test_code_merge, setup=setup_code, number=100000)
print(f"Execution time of merge sort: {execution_time} seconds")
execution_time = timeit.timeit(stmt=test_code_merge2, setup=setup_code2, number=100000)
print(f"Execution time of merge sort 2: {execution_time} seconds")
