arr=input().split(',')
arr=list(map(int,arr))
target=int(input())
lower=0
upper=max(arr)
dic=dict()
for value in range(lower,upper+1):
    temp=arr[:]
    for i in range(len(arr)):
        if temp[i]>value:
            temp[i]=value
    dic[value]=abs(sum(temp)-target)
l=sorted(dic.items(),key=lambda x:x[1])
print(l[0][0])