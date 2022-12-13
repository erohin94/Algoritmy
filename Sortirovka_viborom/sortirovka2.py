"""
Код сортировки выбором, сортируем массив по порядку
"""
def sort_vib(arr):
	N = len(arr) 
	for i in range(N-1):
		naim_zn= arr[i]
		naim_ind= i
		for j in range(i+1, N-1):
			if naim_zn > arr[j]:
				naim_zn = arr[j] 
				naim_ind = j
		# обмен значениями, если был найден минимальный не в i-й позиции
		if naim_ind != i:
			t = arr[i]
			arr[i] = arr[naim_ind]
			arr[naim_ind] = t
	return arr
	
print(sort_vib([5, 3, 6, 2, 10]))
print(sort_vib([-3, 5, 0, -8, 1, 10]))
		
	
