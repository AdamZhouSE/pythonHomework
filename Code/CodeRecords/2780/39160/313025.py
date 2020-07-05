t=int(input())

for i in range(t):
    l = int(input().strip())
    array = list(map(int, input().strip().split()))
    k = int(input().strip())
    mult = 1
    
    for a in array:
        mult *= a
        mult %= k
        if mult == 0:
            break
        
    print(mult)