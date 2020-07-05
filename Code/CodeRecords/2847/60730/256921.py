m = int(input())
n = list(map(int, input().split()))
start, end = map(int, input().split())
sum = 0
for i in range(start, end):
    sum = sum + n[i-1]
print(sum)