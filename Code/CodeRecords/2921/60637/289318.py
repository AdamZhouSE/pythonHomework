n,m,d=map(int,input().split(' '))
arr=[]
for i in range(n):
    arr+=list(map(int,input().split(' ')))
maxNum=max(arr)
minNum=min(arr)
record=float('Inf')
for i in range(minNum,maxNum+1):
    temp=0
    judge=True
    for j in arr:
        if(abs(i-j)%d!=0):
            judge=False
            break
        else:
            temp+=((int)(abs(i-j)/d))
    if(judge and temp<record):
        record=temp
print(record if record!=float('Inf') else -1)

