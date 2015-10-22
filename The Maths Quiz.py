import time
import random


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y

score = 0
operator = 0
question = 0
#This part sets the variables for the question number, score and the operator
print('Welcome to my brilliant maths quiz\n')
time.sleep(1.5)
print()
print('What is your name?')
name = input('Name: ')
print()
print('Welcome to the quiz', name)
#This bit of the code asks for ther users name and then displays that name to the screen
time.sleep(2)
print('Which class are you in? A,B or C')
group = input('Class: ')


if group == 'A' or group == 'a':
    file = open('Class_A_Results.txt', 'a')
if group == 'B' or group =='b':
    file = open('Class_B_Results.txt', 'a')
if group == 'C' or group =='c':
    file = open('Class_C_Results.txt', 'a')

#This bit of the code asks for ther users name and then displays that name to the screen

while question < 10:
#This part sets the number of questions to 10
    n1 = random.randint(0,12)
    n2 =  random.randint(0, 12)
    operator = random.randint (1,3)
#This bit of code sets the boundries for the random numbers and the operators
    
    
    if operator == 1:
       print(n1, "+", n2)
    elif operator == 2:
        print(n1, "-", n2)
    elif operator == 3:
        print(n1, "*", n2)
#This bit determines which operator is shown to the screen
   

    if operator == 1:
        ans = add(n1,n2)
    elif operator == 2:
        ans = subtract(n1,n2)
    elif operator == 3:
        ans = multiply(n1,n2)
#This part sets the answer to the question   

    answer = int(input())
    if answer == ans:
        print("Correct")
        score = score + 1
        
    else:
        print("Incorrect")
    question = question +1
#This part allows the user to put in an answer and tells them if they are right or not
print()
print()
print ('Score = ',score)
file.write(name)
file.write(':')
file.write(str(score))
file.write("\n")
file.close()
if score <=5:
    print ('Unlucky')
else:
    print('Well done')
#This part adds up the score and tells them the score and a message

    
    

