print("enter the number to find factorial:")
a=int(input(""))
factorial=1
if a<0:
    print("factorial not exist in negative number")
elif a==0:
    print("factorial of 0 is 1")
else:
    for x in range(1,1+a):
        
        factorial=factorial*x
    print("factorial of",a,"is",factorial)
