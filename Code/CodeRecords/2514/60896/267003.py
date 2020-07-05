a=input()
b=input()
count=0
count2=0
for i in a:
    while(count<len(b)):
        if(i==b[count]):
            count2=count2+1
            count=count+1
            break
        count=count+1
if(count2==len(a)):print(True)
else:print(False)