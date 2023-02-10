
def sum(num1,num2):
    sum=num1+num2
    print(sum)

def sub(num1,num2):
    sub=num1+num2
    print(sum)

def mul(num1,num2):
    mul=num1*num2
    print(sum)

def div(num1,num2):
    div=num1/num2
    print(div)

num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))

op=str(input("Enter te operator:"))

if op == '+':
 sum(num1,num2) 

elif op=='-':
  sub(num1,num2)

elif op=='*':
 mul(num1,num2)

elif op=='/':
  div(num1,num2)  