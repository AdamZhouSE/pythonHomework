All = int(input())

for q in range(0, All):
    length = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    
    a1.sort()
    a2.sort()
    
    if a1==a2:
        print(1)
    else:
        print(0)