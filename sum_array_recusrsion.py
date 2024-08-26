def sum_array(num_list):
    if len(num_list)==0:
        return 0
    else:
        return (num_list[0])+ sum_array(num_list[1:])

num_list = input("Enter elements of array: ").split()

num_list = list(map(int,num_list))
result= sum_array(num_list)
print(result)

#Demonstration:
num_list = [2,3,4,5,6]
# 2 + [3,4,5,6]
# 2 + 3 + [4,5,6]
# 2 + 3 + 4 + [5,6]
# 2 + 3 + 4 + 5 + [6]
# 2 + 3 + 4 + 5 + 6