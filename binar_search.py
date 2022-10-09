""" 
list1 = [1, 3, 5, 7, 9]
guess1 = list1[2]
print(guess1)
Получим значение 5, так как обратились 
к третьему элементу списка list1, отсчет идет с нуля,
по этой же причине пишем high = len(list)-1.

Если после guess в цикле поставить print(guess),
        mid = (low + high)//2
        guess = list[mid]
        print(guess)
то увидим за сколько итераций выполнится код.
"""

def binary_search(list, item):
	# в low и high хранятся границы части списка, где выполняется поиск
    low = 0
    high = len(list)-1 #-1 так как обращаемся к аргументу списка, длина будет 5, а аргументы идут с 0,1,2,3,4 соответственно 5-го нет.
    # Пока не останется один элемент
    while low <= high:
		# Проверяем средний элемент
        mid = (low + high)//2
        guess = list[mid]
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


my_list = [1, 3, 5, 7, 9]
# Выводит порядковый номер искомого элемента
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


