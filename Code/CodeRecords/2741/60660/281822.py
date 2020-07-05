l=eval(input())
m=0;sum=1;
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        sum+=1
    else:
        m=max(m,sum)
        sum=1
print(m)