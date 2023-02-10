
def factorial(num):
   fact=num
   for i in range(1,num): 
       
     fact=fact* i

   print(fact)


num=int(input("Enter the number"))

factorial(num)