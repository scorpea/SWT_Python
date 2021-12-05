# Alcohol limit and associated punishment
# Write a drunk driving application that decides if a driver is above alcohol limit and give an appropriate punishment
try:
    dname = input("Enter Driver's Name: ")
    alcohol_level = float(input("Enter the Alcohol Level: "))

    print("Alcohol Level for ", dname, "is ", alcohol_level,"mg")
    if alcohol_level == 0:
        print("The Driver is OK and no fine/punishment is needed")

    elif alcohol_level > 0 and alcohol_level <= 0.2:
        print("The Driver is OK but has Alcohol in the blood")

    elif alcohol_level > 0.2 and alcohol_level < 0.5:
        print("Alcohol level in the blood is unaccepted ")
        print("The Driver has the sum of 20,000kr to pay")
        print("The Driver has a 1 Year ban as punishment")

    elif alcohol_level > 0.5:
        print("Alcohol level in the blood is unaccepted ")
        print("The Driver fine is 10% of yearly salary")
        print("The Driver has a 3 Year ban and 6 months in prison as punishment")

    else:
        print("The Alcohol level entered is out of range")
except:
    print("invalid entry")