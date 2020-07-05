n=int(input())
numbers=list(map(int,input().split(" ")))
numbers.sort()
count=0
for i in range(1,n+1):
    count=count+abs(i-numbers[i-1])
print(count)