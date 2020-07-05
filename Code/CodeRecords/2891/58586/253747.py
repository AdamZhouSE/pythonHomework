nums=int(input())
arr=list(map(int,input().split(" ")))
largest=max(arr)
sum=0
for i in arr:
    sum+=(largest-i)
print(sum)