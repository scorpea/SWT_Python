# Python program to determine the largest in a list
numb_list = [7,1,12,3,4,8,0]
largest = max(numb_list)
#print("the Largest number in the list is ", largest)
max_numb = numb_list[0]
for num in numb_list:
    if num > max_numb:
        max_numb = num
print(max_numb)
