A=list(map(int,input().strip().split(',')))
B=list(map(int,input().strip().split(',')))
C=list(map(int,input().strip().split(',')))
D=list(map(int,input().strip().split(',')))
ABsum=dict()
res=0
for i in A:
    for j in B:
        temp=i+j
        if temp not in ABsum:
            ABsum[temp]=1
        else:
            ABsum[temp]+=1
for i in C:
    for j in D:
        temp=i+j
        if -temp in ABsum:
            res+=ABsum[-temp]
print(res)