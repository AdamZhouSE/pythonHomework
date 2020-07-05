n=int(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]
if sum(arr)%2==0:
    print("YES")
else:
    print("NO")