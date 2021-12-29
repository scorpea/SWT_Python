# Write a python program
# Define a student loan function
# Only students that have an income are eligible for a loan
# All students without an income will get the message "Sorry, you are not eligible for a loan"

# If a student earns below 15,000 they get a loan at 30% yearly interest and a duration of 5 years
# Print out the monthly payment in this case for the student

# Students earning 15,000 and above can get a loan with a yearly interest of 10% and a duration of 7 years
# Print out the monthly payment in this case for the student

# You need to input the loan amount, duration and the interest to calculate the monthly payment and print it out.

def stud_loan(loan_amt,interest,m_year):
    month_pay = loan_amt * (interest * (1 + interest) ** m_year) / ((1 + interest) ** m_year - 1)
    return month_pay

# Main Program
print("W E L C O M E   T O   S T U D E N T   L O A N   S Y S T E M")
try:
    loan_amt = int(input("Enter the Loan you want to apply for (kr):- "))
    inc_check = input("Do you earn an Income today [Y/N]:- ")
    if inc_check.upper() == "Y":
        income = int(input("Enter yearly income (kr):- "))
        if income < 15000:
            int_rate = 30
            interest = (30 / 100) / 12
            year = 5
            m_year = year * 12
        else:
            int_rate = 10
            interest = (10 / 100) / 12
            year = 7
            m_year = year * 12
        print("")
        print("Your monthly Payment for", '{:,.2f}kr'.format(loan_amt), "at", str(int_rate) + "% for", year, "years is",'{:,.2f}kr'.format(stud_loan(loan_amt,interest,m_year)))
    elif inc_check.upper() == "N":
       print("Sorry, you are not eligible for a loan")
    else:
        print("Y or N expected. Try again ")
except:
    print("Numeric Value expected, Try again")