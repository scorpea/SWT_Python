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

# Extract all the digits and print to the terminal
xdigit = re.findall("\d", searchstr)
print("The Digits in the Text are ", xdigit)

# my own reasoning to print digits same way they appear in the text
# count the spaces
print("")
print("Arnold's Reasoning of printing the way the numbers appeared in the text")
space_num = searchstr.count(" ")
for i in range(0,space_num):
    space_detect = re.search("\s", searchstr)
    strdigit = searchstr[:space_detect.start()]
    if strdigit.isdigit():
        print(strdigit)
    searchstr = searchstr[space_detect.start() + 1:]




