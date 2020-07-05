nums=int(input())
sum1=0
sum2=0
valid1=0
valid2=0
for i in range(nums):
    arr=list(map(int,input().split(" ")))
    if arr[0]==1:
        sum1+=10
        valid1+=arr[1]
    else:
        sum2+=10
        valid2+=arr[1]
if valid1>=sum1//2:
    print("LIVE")
else:
    print("DEAD")
if valid2>=sum2//2:
    print("LIVE")
else:
    print("DEAD")