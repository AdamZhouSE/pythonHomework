count = int(input())

while count > 0:
    n, k = map(int,input().split())
    print(k**(n-1))
    count -= 1
