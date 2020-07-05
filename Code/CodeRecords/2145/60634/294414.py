import sys
test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split(' ')

    S = 0
    
    mem = []
    for x in range(n):
        mem.append(sys.maxsize)
        arr[x] = int(arr[x])
    
    l = 1
    while l <= n:
        i = 0
        while i <= n - l:
            if arr[i+l-1] < mem[i]:
                mem[i] = arr[i+l-1]
            temp = mem[i]*l
            if temp > S:
                S = temp
            i += 1
        l += 1
    
    print(S)

