a=input()
b=eval(a)
c=b.copy()
c.sort()
count1=0
count2=0
for i in range(0,len(c)):
    if(b[i]!=c[i]):
        break
    else:
        count1+=1
for i in range(len(c)-1,-1,-1):
    if(b[i]!=c[i]):
        break
    else:
        count2+=1
print(len(c)-count1-count2)