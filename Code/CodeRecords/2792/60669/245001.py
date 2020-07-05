n=int(input())
arr=list(map(int,input().split()))
t=arr.count(1)
result=[]
for i in range(0,len(arr)-1):
    front=arr[i]
    behind=arr[i+1]
    if front==1 and behind==1:
        result.append(1)
    if front!=1 and behind==1:
        if i+1==len(arr)-1:
            result.append(front)
            result.append(1)
        else:
            result.append(front)
    elif i+1==len(arr)-1:
        result.append(behind)
print(t)
string="".join([str(x)+" " for x in result])
print(string.strip())

