target=int(input())
sum = 0
n = 0
target = abs(target)
while(1):
    if sum >= target:
        if sum == target or (sum - target) % 2 == 0:
            print(n)
        elif n % 2 == 0:
            print( n + 1)
        else:
            print( n + 2)
    n = n + 1    
    sum = sum + n