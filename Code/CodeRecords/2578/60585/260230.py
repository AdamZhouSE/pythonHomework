arr=list(map(int,input().strip().split(',')))
threshold=eval(input())
res=1
isFound=False
while True:
    sum=0
    for i in arr:
        if i%res==0:
            sum+=i//res
        else:
            sum+=i//res+1
    if sum<=threshold:
        isFound=True
        break
    if isFound:
        break
    res+=1
print(res)