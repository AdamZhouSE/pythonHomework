All = int(input())

for q in range(0, All):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    
    print(ar[-1]*ar[-2]*ar[-3])