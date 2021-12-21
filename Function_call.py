# Python Program that calls a function to add, subtreact, multiply and divide numbers
# w,x,y,z = input("Enter values for 4 numbers separating with a space ").split()


# Addition Function Defined
def numb_add(numb):
   try:
      sum_numb = 0
      for i in range(0,int(n)):
         sum_numb = sum_numb + int(numb[i])
      return sum_numb
   except:
      print("Error, none numeric entered")

# Subtraction Function Defined
def numb_sub(numb):
   try:
      sub_numb = int(numb[0])
      for i in range(1,int(n)):
         sub_numb = sub_numb - int(numb[i])
      return sub_numb
   except:
      print("Error, none numeric entered")

# Multiplication Function Defined
def numb_mul(numb):
   try:
      mul_numb = 1
      for i in range(0,int(n)):
         mul_numb = mul_numb * int(numb[i])
      return mul_numb
   except:
      print("Error, none numeric entered")

# Division Function Defined
def numb_div(numb):
   try:
      div_numb = int(numb[0])
      for i in range(1,int(n)):
         div_numb = div_numb / int(numb[i])
      return div_numb
   except:
      print("Error, none numeric entered")

#Main Program
numb = []
n = input("How many numbers do you want to Add, Subtract, Multiply or divide:- ")
if n.isdigit():
   for i in range(0,int(n)):
      numb.append(input("Enter a number accordingly:- "))
   numb_op = input("Choose the operator you want? [A]ddition, [S]ubtraction, [M]ultiplication, [D]ivision ")
   print()
   if numb_op.upper() == "A":
      print("The Addition of the above numbers entered is", numb_add(numb))
   elif numb_op.upper()  == "S":
      print("The Subtraction of the above numbers entered is", numb_sub(numb))
   elif numb_op.upper()  == "M":
      print("The Multiplication of the above numbers entered is", numb_mul(numb))
   elif numb_op.upper() == "D":
      nd = numb_div(numb)
      print("The Division of the above numbers entered is " '{:,.2f}'.format(nd))
   else:
      print("Allowed inputs are A, S, M or D. Try again")
else:
   print("Number expected, Try again!")