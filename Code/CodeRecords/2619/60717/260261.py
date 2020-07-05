n=int(input())
for i in range(0,n):
    tmp=input()
    for j in tmp:
        flag=1
        if tmp.count(j)>1:
            flag=0    