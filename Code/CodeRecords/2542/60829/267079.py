bb=str(input())
b=[]
for i in bb:
    if not i=="," and not i=="[" and not i=="]" and not i==" ":
        b.append(int(i))
b.sort()
count1=1
count2=1
for i in range(0,len(b)-1):
    if b[i+1]==b[i]+1:
        count1=count1+1
    else:
        if count1>=count2:
            tmp=count1
            count1=count2
            count2=tmp
        else:
            count=1
print(count2)