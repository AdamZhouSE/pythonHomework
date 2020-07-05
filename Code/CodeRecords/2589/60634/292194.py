#main-----
test = int(input())
for t in range(test):
    n = int(input())
    
    l1 = 1
    l2 = 2
    lucas = 1
    i = 2
    while i <= n:
        lucas = l1 + l2
        l2 = l1
        l1 = lucas
        i += 1
    print(lucas)