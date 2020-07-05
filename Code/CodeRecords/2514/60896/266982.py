a=input()
b=input()
count=0
for i in a:
    while(count<len(b)):
        if(i==b[count]):
            count=count+1
            break
        count=count+1
if(count<=len(b)):print(True)
else:print(False)