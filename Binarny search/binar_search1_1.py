"""
Грокаем алгоритмы, Упражнение 1.1; 1.2
Имеется отсортированный список из 128 имен, 
и вы ищете в нем значение методом бинарного поиска. 
Какое максимальное количество проверок для этого может потребоваться?
"""
def binary_search(list, item):
	# в low и high хранятся границы части списка, где выполняется поиск
    low = 0
    high = len(list)-1
    # Пока не останется один элемент
    spisok_itterac = []
    while low <= high:
		# Проверяем средний элемент
        mid = (low + high)//2
        guess = list[mid]
        spisok_itterac.append(guess)
        print('Номер иттерации ' + str(len(spisok_itterac)))
        # Значение найдено
        if guess == item:
            return mid
        # Значение велико   
        if guess > item:
            high = mid - 1
        # Значение мало    
        else:
            low = mid + 1
    # Значение не найдено        
    return None

# Допустим, вместо имён я буду использовать цифры
data = [i for i in range(1, 256)]  
print(binary_search(data, 22))

# Ответ 7 итераций, последняя итерация это 21
