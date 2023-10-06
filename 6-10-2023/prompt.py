a=[]
n=int(input("enter length of list:"))
print("enter the element:")
for i in range(0,n):
    e=int(input(""))
    if e<=100:
         
         a.append(e)
    else:
        a.append("over")
    
print(a)
    
