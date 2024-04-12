# Python Program to Guess a correct Number
right_numb = 7
tr = 3
print("You have 3 trails to Guess a number between 1 and 9")
for i in range(tr):
    print('Trail ',i+1)
    x = int(input('Guess a number '))
    if x <= 0:
        print("The number must be a whole number")
    elif x == right_numb:
        print("Hurray, You guessed the right number")
        break
    else:
        print("The number entered is not correct")










