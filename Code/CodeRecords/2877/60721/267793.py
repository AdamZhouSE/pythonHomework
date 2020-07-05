n=int(input())
lis=list(map(int,input().split(" ")))
re=0
re1=0
for i in lis:
    if i>=0:
        re+=i
    else:
        re1+=i
if(re1==0):
    print(re)
else:    
    print(re-re1)