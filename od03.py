import time
import random
#Пузырьковая сортировка
mas = [random.randint(0,1000) for i in range(100)]
# mas = [5,2,8,11,4,2,8,10,2]
n = len(mas)
start_time = time.time()
for i in range(n):
    for j in range(0, n-i-1):
        if mas[j] > mas[j+1]:
            mas[j], mas[j+1] = mas[j+1], mas[j]
end_time = time.time()
execution_time = (end_time - start_time)*1000
print(mas)
print(f'Время выполнения: {execution_time:.6f} мс')

# Сортировка выбором
mas1 = [random.randint(-1000,1000) for i in range(100)]
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
start_time = time.time()
selection_sort(mas1)
end_time = time.time()
execution_time = (end_time - start_time)*1000
print(mas1)
print(f'Время выполнения: {execution_time:.6f} мс')