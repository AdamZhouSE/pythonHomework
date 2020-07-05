n=int(input())
lis=list(map(int,input().split(" ")))
lis=sorted(lis)
m=int(input())
lis_op=[]
for i in range(0,m):
    lis_op.append(input().split(" "))
for i in lis_op:
    if len(i)==1:
        print(lis[(len(lis)+1)//2-1])
    else:
        lis.append(int(i[1]))
        lis=sorted(lis)