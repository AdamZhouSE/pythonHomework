t = int(input())
for i in range(t):
    n, k = map(int,input().split(" "))
    toys = list(map(int,input().split(" ")))
    toys.sort()
    current = 0
    num = 0
    j = 0
    while current<=k and j<len(toys):
        current += toys[j]
        j+=1
        num+=1
    print(num-1)