list=["farook","rishan","arun","ansar"]
count=0
a='a'
print(list)
for i in list:
    for f in i:
        if(f == a):
            count=count+1
print("count of",a,"in",list,"is",count)
