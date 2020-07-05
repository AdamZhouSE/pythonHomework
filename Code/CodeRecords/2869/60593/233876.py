n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
arr=list(set(arr))
for i in arr:
    print(i,'',end='')