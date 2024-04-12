# Python Program to check the date validity for a flight for year 2022
# Fuction to the check the validity of date entered
import datetime


def check_date(y, m, d):
    cdate = None
    try:
        ndate = date(int(y), int(m), int(d))
        cdate = True
    except ValueError:
        cdate = False
    return cdate

#Main Program
from datetime import *
dtime = datetime.now().strftime("%a %Y-%m-%d %H:%M %p")
print("W E L C O M E   T O   A R N Y   D A T E   C H E C K I N G   S Y S T E M")
print(dtime)
print("")
ctime = datetime.time(datetime.now() + timedelta(hours=10))
otime = time

print(ctime)
try:
    y,m,d = input("Enter the date of departure (yyyy-mm-dd):- ").split("-")
    edate = date(int(y), int(m), int(d))
    if check_date(y,m,d):
        if date.today() > edate:
            print("⚠️ Error! Past date can not be entered")
        else:
            print("✅ Date is valid")
    else:
        print("⛔ Invalid date entered!")
except:
    print("⛔ Invalid date entered!!")
