
def reverse (my_list,i,j):
 while i<=j :
   temp=my_list[i];
   my_list[i]=my_list[j];
   my_list[j]=temp;
   i+=1
   j-=1
my_list=[1,3,4,5,6,78,9]
reverse(my_list,0,6)
print(my_list)