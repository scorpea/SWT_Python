# Write a python program that does below:
#-----------------------------
# Ask the user to input a temperature in °F
# Convert the temperature entered from to °C
# if temperature is greater than 30
# print "it's a hot day"
# otherwise if it's less than 10
# print "it's a cold day"
# otherwise
# print "it's neither hot nor cold"


print("Daily Temperature Check")
tempf = input("Enter Temperature in °F:- ")
if tempf.isdigit():
    tempc = (float(tempf) - 32) / 1.8
    print("Temperature entered in celsius:- " '{:.2f}°C'.format(tempc))
    if round(tempc) > 30:
        print("it's a hot day")
    elif round(tempc) < 10:
        print("it's a cold day")
    else:
        print("it's neither hot nor cold")
else:
    print("Number value is expected, Try again")


