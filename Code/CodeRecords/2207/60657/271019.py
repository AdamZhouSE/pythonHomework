n=int(input())
def cal(a,b):
    sum=0
    for i in range(1,b+1):
        sum+=i
    if a>sum:
        return 1
    else:
        return 0
for i in range(n):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print(cal(arr[0],arr[1]))