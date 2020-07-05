n,m=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
lis1=list(map(int,input().split(" ")))
re=[]
for i in range(0,len(lis)):
    if lis[i] in lis1:
        re.append(lis[i])
for i in range(0,len(re)):
    print(re[i],end="")
    if(i!=len(re)-1):
        print(" ",end="")
print()