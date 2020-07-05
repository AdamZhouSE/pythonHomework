T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    num,x=arr[0],arr[1]
    result=num-x+1
    result=0-result
    print(result)
