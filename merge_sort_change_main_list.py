def merge(list, left_list, right_list):
	
	index = 0
	
	index2 = 0
	
	index3 = 0
	
	while index < len(left_list) and index2 < len(right_list):
		
		if left_list[index] < right_list[index2]:
			
			list[index3] = left_list[index]
			
			index += 1
			
		else:
			
			list[index3] = right_list[index2]
			
			index2 += 1
			
		index3 += 1
		
	while index < len(left_list):
			
			list[index3] = left_list[index]
			
			index += 1
			
			index3 += 1
			
	while index2 < len(right_list):
			
			list[index3] = right_list[index2]
			
			index2 += 1
			
			index3 += 1	
			
			
def merge_sort(list):
	
	if len(list) < 2:
		
		return
		
	mid = len(list) // 2
	
	left_list = list[ : mid]
	
	right_list = list[mid : ]
	
	merge_sort(left_list)
	
	merge_sort(right_list)
	
	merge(list, left_list, right_list)
	
	
list = list(map(int, input("Please enter the items of list:\n").split()))

merge_sort(list)

print("Sorted list:")

print(list)