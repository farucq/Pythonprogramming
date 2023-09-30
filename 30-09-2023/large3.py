print("enter three numbers")
a=int(input(""))
b=int(input(""))
c=int(input(""))
if (a>b) & (a>c):
    print("largest no:",a)
elif (b>a) & (b>c):
     print("largest no:",b)
else:
    print("largest no:",c)
