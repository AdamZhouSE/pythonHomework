t = int(input())
for i in range(t):
    nm = list(map(int, input().split()))
    n = nm[0]
    money = nm[1]
    result = int((n-1)/2)+1
    print(result * money)