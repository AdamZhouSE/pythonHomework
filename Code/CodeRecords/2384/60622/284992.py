num=int(input())
for i in range(num):
    n=int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max_=arr[-1]+1
    for i in range(1,max_+1):
        if i not in arr:
            print(i)
            break
