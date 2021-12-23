# convert for loop to while
solomon = 0
while solomon <= 20:
    if (solomon % 2) != 0:
        print(solomon)
    solomon = solomon + 1



#Printing *
try:
    n = int(input("How many times do you want the loop to run:- "))
    i = 1
    st = "*"
    while i <= n:
        print(st * i)
        i = i +1
except:
    print("Number required, try again")