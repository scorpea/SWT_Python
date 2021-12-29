# Mortgage Function Call -PMT which calculate your monthly payment based on the principal, interest and
# number of payments

def pmt(p,i,n):
    i= (i / 100) / 12
    n = n * 12
    month_pay = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return month_pay

# Main Program
try:
    p = int(input("Enter the principal Amount(kr):- "))
    i = int(input("Enter the interest rate (%):- "))
    n = int(input("Enter the duration (number of years):- "))
    print("")
    print("The Monthly payment calculated for",p,"kr at",i,"% per annual for",n,"years is ",'{:,.2f}kr'.format(pmt(p,i,n)))
except:
    print("Numeric Value expected, Try again")