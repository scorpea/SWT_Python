# Write a program to remove the duplicates in a list
duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7]

new_list = []
for num in duplicate:
    if num not in new_list:
       new_list.append(num)

print("Ordinary List " + str(duplicate))
print("")
print("After duplication removal " + str(new_list))
