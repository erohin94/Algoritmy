"""
Код выполняет сортировку массива по возрастанию. 
Напишем функцию для поиска наименьшего элемента массива.
"""
def findSmallest(arr):
	#хранение наименьшего значения
	smallest = arr[0]
	#хранение индекса наименьшего значения
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	#выводим номер индекса, а не наименьшее число
	return smallest_index

print(findSmallest([5, 3, 6, 2, 10]))

"""
На основе этой функции findSmallest,
можно написать функцию сортировки выбором
"""
#сортирует массив
def selectionSort(arr): 
	newArr = []
	for i in range(len(arr)):
		#Находит наименьший элемент в массиве и добавляет его в новый массив
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))
