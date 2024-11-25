'''
# Main calculator function parameters for the calculator function
takes the following parameters:
        num 1
        num 2
        operand

Add the the inputs with the operand

====OUTPUT=====
result 
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
operand = input("Enter the operand as +, -, *, /, % :  ")

if operand ==  '+':
    result = str(num2+num1) + "\n  Operation: Addition" 
    
elif operand == '-':
    result = str(num1 - num2) + "\n Operation: Subtraction" 
    
elif operand == '*':
    result = str(num2 * num1) + "\n Operation: Multiplication" 

elif operand == '/':
    result = str(num1 / num2) + "\n Operation: Divisions" 
    
elif operand == '%':
    result = str(num1 % num2) + "\n Operation: Modulus"
    
else:
    result = " Enter the stipulated operands"

print(result)