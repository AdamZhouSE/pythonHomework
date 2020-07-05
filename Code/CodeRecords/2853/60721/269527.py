n=int(input())
lis=list(map(int,input().split(' ')))
count=0
for i in lis:
    if(i%2!=0):
        count+=1
if(count%2==0):
    print(len(lis)-count)
else:
    print(count)
