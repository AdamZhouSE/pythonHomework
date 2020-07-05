n=int(input())
for i in range(0,n):
    numlist=input().split(' ')
    k=int(numlist[0])
    sum=int(numlist[1])
    mat1=[]
    mat2=[]
    res=0
    for j in range(0,k):
        numlist=list(map(int,input().split(" ")))
        mat1.extend(numlist)
    for j in range(0,k):
        numlist = list(map(int, input().split(" ")))
        mat2.extend(numlist)
    for j in mat1:
        tar=sum-j
        res+=mat2.count(tar)
    print(res)