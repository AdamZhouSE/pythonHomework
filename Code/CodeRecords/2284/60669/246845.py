t=int(input())
num=int(input())
arr=list(map(int,input().split()))
temp=[]
for i in range(0,len(arr)):
    left=arr[i]
    dis=0
    while True:
        if i==len(arr)-1-dis:
            temp.append(0)
            break
        right=arr[len(arr)-1-dis]
        if left<right:
            temp.append(len(arr)-1-dis-i)
            break
        else:
            dis+=1
print(max(temp))