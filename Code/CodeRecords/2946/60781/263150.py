n=input()
lenth=len(n)
i=0
count=0
while i<lenth-1:
    if(n[i]!=n[i+1]):
        count+=1
    i+=1
if(n[lenth-1]=='0'):
    print(count+1,end='')
else:    
    print(count,end='')
