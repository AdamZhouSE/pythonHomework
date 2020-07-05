def solve(n,arr):
    mem = []
    for x in range(n):
        arr[x] = int(arr[x])
        mem.append({arr[x]})
        
    count = n
    l = 2
    while l <= n:
        i = 0
        while i <= n - l:
            if mem[i] != None:
                if arr[i+l-1] in mem[i]:
                    mem[i] = None
                else:
                    mem[i].add(arr[i+l-1])
                    count += l
            i += 1
        l += 1
    
    return count



#main-----
test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split(' ')
    print(solve(n,arr))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    