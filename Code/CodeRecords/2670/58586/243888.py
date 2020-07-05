nums=int(input())
for i in range(nums):
    num=int(input())
    arr=[]
    while num>0:
        arr.append(1^(num%2))
        num=num//2
    sum=0
    i=len(arr)-1
    while i>=0:
        sum=sum*2+arr[i]
        i-=1
    print(sum)