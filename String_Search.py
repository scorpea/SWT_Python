#String search
import re
#•	Extract the non-repeated phrase and print to the terminal

str1 = "What is the main reason for leaving? 21 Happy Easter Holidays 40 All the men here are just not understanding the "
str2 = "situation Happy Easter Holidays 50 In what ways can I help you Happy Easter Holidays You better learn how to be "
str3 = "polite 100 Happy Easter Holidays OMG that food is looking really great Happy Easter Holidays 100 800 900"

searchstr = str1 + str2 + str3
searchstr = searchstr.upper()
print(searchstr)
print("")
substr = input("Enter a word or phrase yu want to search from the above text ")
substr1 = substr.upper()

# Count the number of times the phrase occured and print to the terminal
cphrase = searchstr.count(substr1)
print(substr, "occurs in the text",cphrase,"times")
print("")

# Extract all the numbers and print to the terminal
x = re.findall("\d", searchstr)
print(x)

# my reasoning
strlen = len(searchstr)
print(strlen)

sp = re.search("\s", searchstr)
print("")
print("The first white-space character is located in position:", sp.start())

# count the spaces
x1 = searchstr.count(" ")
print("")
print("Number of space available are ",x1)

nums = ""
for i in searchstr:
    if i.isdigit() and i != "\s":
        nums = nums + i
        print(nums)


#    print(i,end="")

#



