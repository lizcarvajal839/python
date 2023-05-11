def check_sum(num_list):
     # Replace with your code
    found=False
    for i in range(0,len(num_list)):
        for j in range(1,len(num_list)):
            if num_list[i]+num_list[j]==0:
                found=True
    return found 

num_list=[10, -14, 26, 5, -3, 13, -5]
list2=[10, -14, 26, 5, -3]
print(check_sum(num_list))
print(check_sum(list2))
