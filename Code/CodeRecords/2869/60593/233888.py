n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
arr=list(set(arr))
print(len(arr))
for i in range(len(arr)):
    if(i==len(arr)-1):
        print(i)
    else:
        print(i,'',end='')