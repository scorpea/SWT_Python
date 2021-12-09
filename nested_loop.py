# Nested Loops
# Generating a X, Y coordinators
print("X and Y coordinates")
# x = 0
# while x <= 2:
#    y = 0
#    while y <= 2:
#        print("("+str(x)+","+str(y)+")")
#        y = y + 1
#     x = x +1

for x in range(0,3):
    for y in range(0,3):
        print("("+str(x)+","+str(y)+")")