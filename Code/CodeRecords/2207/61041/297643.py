t=eval(input())
for i in range(0,t):
    arr=input().split()
    A=int(arr[0])
    B=int(arr[1])
    sum=0
    for j in range(1,B+1):
        sum+=j
    if sum<=A:
        print(1)
    else:
        print(0)