import array
import sys

num_list = []
tot_num = int(raw_input("enter the number of elements you want in a list: "))
count = 0
while (count < tot_num):
	num = int(raw_input("Enter the %s number: " %count))	
	num_list.append(num)
	count = count+1
arr_num = 0
min_num = num_list[0]
min_loc = 0
i = 0
print ("Entered list %s"%num_list)
while( i < tot_num):
	min_num = num_list[i]
	arr_num = i
	while(arr_num < tot_num-1):
		if min_num > num_list[arr_num+1]:
			min_num = num_list[arr_num+1]
			min_loc = arr_num+1
			arr_num = arr_num+1
			flag = 0
		else:
			arr_num = arr_num+1
			flag = 1
	if (flag == 0):
		temp = num_list[i]
		num_list[i] = min_num
		num_list[min_loc] = temp
	i = i+1
print ("sorted list %s"%num_list)		
