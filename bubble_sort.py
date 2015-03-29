import sys
import array

tot_num = int(raw_input("enter the number of values you want in a list: "))
num_list=[]
count = 1
while (count <= tot_num):
	value = int(raw_input("Enter value %s " %count))
	num_list.append(value)
	count = count + 1
print ("Entered list of Numbers %s " %num_list)

tot_itr = 0
while (tot_itr < tot_num):
	sort_iteration = 0
	while (sort_iteration < tot_num-1):
	
		if num_list[sort_iteration] > num_list[sort_iteration+1]:
			temp = num_list[sort_iteration]
			num_list[sort_iteration] = num_list[sort_iteration+1]
			num_list[sort_iteration+1] = temp
			sort_iteration = sort_iteration+1
		else:
			sort_iteration = sort_iteration+1
	tot_num = tot_num-1
	tot_itr = tot_itr+1
print("Sorted list of entered number %s " %num_list)	
