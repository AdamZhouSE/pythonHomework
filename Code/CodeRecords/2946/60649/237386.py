n=input()
k=len(n)
count=0
for i in range(k-1):
    if(n[i]!=n[i+1]):
        count+=1
if(n[k-1]=='0'):
    count+=1
print(count,end='')