my_list = [1, 4, 5, 8, 10]
  
flag = 0
i = 1
while i < len(my_list):
    if(my_list[i] < my_list[i - 1]):
        flag = 1
    i += 1
     
if (not flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")