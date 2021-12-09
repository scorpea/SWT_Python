# Take as input the price of a house for sale
# if a buyer has good credit, they gets 10% of the price else 20%
#take as input the customer's yearly income
#print out the down payment on if the user has good credit or not

print("House for Sale!")
good_credit = 500000
house_sale = input("Enter the price of the House (kr):- ")
if house_sale.isdigit():
    year_income = input("Enter your yearly income (kr):- ")
    if year_income.isdigit():
        if int(year_income) >= good_credit:
            downpay = int(house_sale) * 0.1
            print("Your Down payment for the house is :- " '{:,.2f}kr'.format(downpay))
        else:
            downpay = int(house_sale) * 0.2
            print("Your Down payment for the house is :- " '{:,.2f}kr'.format(downpay))
    else:
        print("Integer input required, try again")
else:
    print("Integer input required, try again")


