def calculate():
    number1 = int(input('enter a number: '))
    number2 = int(input('enter another number: '))
    operation = input('''
Enter a operation please:
+ for addition
- for subtraktion
* for multiplikation
/ for division
''')
    if operation == '+':
        number = number1 + number2
        print(f"{number1} + {number2} = {number}")
    elif operation == '-':
        number = number1 - number2
        print(f"{number1} - {number2} = {number}")
    elif operation == '/':
        number = number1 / number2
        print(f"{number1} / {number2} = {number}")
    elif operation == '*':
        number = number1 * number2
        print(f"{number1} * {number2} = {number}")
    else: 
        print("invalid choose..!")
        
    playAgain()

'''
Do you want to continue?
'''
def playAgain():
    Q = input('do you want to continue?')
    if Q.lower()== "y":
        calculate()
    elif Q.lower()== "n":
        print ("Goodbye my friend!")
    else:
        
        print("invalid choose...!")
        playAgain()
    
calculate()

my_tuple=("name","hanieh niazi")
