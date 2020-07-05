from math import sqrt
# 36
def test():
    n = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    arr.sort(reverse=True)
    for i in range(0, len(arr)):
        if  arr[i]<0:
            print(arr[i])
            return
        elif sqrt(arr[i]) % 1 != 0 and arr[i]>=0:
            print(arr[i])
            return 
        
test()