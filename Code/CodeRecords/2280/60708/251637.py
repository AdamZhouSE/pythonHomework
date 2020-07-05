Q=int(input())#问题数
result=[0]*Q
for i in range(0,Q):
    l=int(input())
    tempstr=input().split(" ")
    lsitNum=[]
    for item in tempstr:
        lsitNum.append(int(item))
    for x in range(0,l-1):
        if lsitNum[x]!=x+1:
            result[i]=x+1
            break
    if lsitNum[l-2]==l-1:
        result[i]=l
    if lsitNum[0]!=1:
        result[i]=1
for item in result:
    print(item)