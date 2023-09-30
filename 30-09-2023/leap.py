y1=int(input("enter current year"))
y2=int(input("enter the future year"))
for year in range(y1,y2):
    if((year%4==0)&(year%100!=0)|(year%400==0)):
        print(year)
    

