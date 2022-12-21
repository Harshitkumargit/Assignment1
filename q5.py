import math

l=int(input("Enter the angle "))
for i in range(0,345,15):
    a=round(math.sin(i),4)
    b=round(math.cos(i),4)
    print(i,a,b)
