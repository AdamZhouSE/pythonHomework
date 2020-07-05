import math
n=int(input())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

for item in arr:
    if item<0:
        print(item)
        break
    elif math.sqrt(item).is_integer()==False:
        print(item)
        break