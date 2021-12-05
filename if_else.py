# Write a python program that will print out the grades based on your input

score = float(input("Enter the student score: "))
print(score)

if score >= 0 and score < 40:
    print("The student grade is F")

elif score >= 40 and score < 45:
    print("The student grade is E")

elif score >= 45 and score < 50:
    print("The student grade is D")

elif score >= 50 and score < 60:
    print("The student grade is C")

elif score >= 60 and score < 70:
    print("The student grade is B")

elif score >= 70 and score <= 100:
    print("The student grade is A")

else:
    print("The value entered is out of range")