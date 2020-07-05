n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
arr=list(set(arr))
arr.reverse()
for i in arr:
    print(i,' ',end='')