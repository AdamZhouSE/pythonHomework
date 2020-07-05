l=list(input())
count=0
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        count+=1
if l[-1]=='0':
    count+=1
print(count,end="")