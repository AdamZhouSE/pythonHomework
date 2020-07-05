n=int(input())
lis=list(input())
color=lis[0]
count=0
for i in range(1,n):
    if(color==lis[i]):
        count+=1
    else:
        color=lis[i]
print(count)