n=int(input())
lis=list(map(int,input().split(" ")))
re=[0 for i in lis]
for i in lis:
    re[i-1]=lis.index(i)+1
for i in range(0,len(re)):
    print(re[i],end="")
    if(i!=len(re)-1):
        print(" ",end="")
print()