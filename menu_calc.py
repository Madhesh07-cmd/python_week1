a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
def add(num1, num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2  
def div(num1,num2):
    if num2==0:
        return "Error"
    else:
        return num1 / num2
switch=input("Enter the operation you want to perform (+, -, *, /): ")
if switch=="+":
    print(add(a,b))
elif switch=="-":
    print(sub(a,b))
elif switch=="*":
    print(mul(a,b)) 
elif switch=="/":    
    print(div(a,b))
    