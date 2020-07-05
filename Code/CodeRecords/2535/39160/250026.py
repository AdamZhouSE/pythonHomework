import sys, os, io

arr = eval(input())

ma=0
ans=0
for i in range(len(arr)):
    ma=max(arr[i],ma)
    if ma==i:
        ans+=1

print(ans)