# Python Program to Guess a correct Number
right_numb = 7
tr = 3
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










