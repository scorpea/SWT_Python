# A python program to change a digit entered to word
num_word = ["Zero", "One","Two", "Three", "Four", "Five", "Six", "Seven","Eight", "Nine"]
num_dig = input("Enter a Telephone number:- ")
print("")
if num_dig.isdigit():
    print("Telephone Number accepted, please wait while I do the word translation")
    for i in num_dig:
        print(num_word[int(i)], end=" ")
else:
    print("Error, digits expected, try again")
