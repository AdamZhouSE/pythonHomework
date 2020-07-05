temp=list(input())
if(temp[0]=='-'):
    i=1
else:
    i=0
j=len(temp)-1
while(i<j):
    now=temp[i]
    temp[i]=temp[j]
    temp[j]=now
    i+=1
    j-=1
for i in range(len(temp)):
    if(temp[i]=='0'):
        del temp[i]
    else:
        break
temp=''.join(temp)
print(temp)
