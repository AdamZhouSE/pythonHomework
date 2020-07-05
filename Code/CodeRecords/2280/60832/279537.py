All = int(input())

for q in range(0, All):
    n = int(input())
    ar = list(map(int, input().split()))

    for i in range(0,n-2):
        if ar[i+1]-ar[i]>1:
            print(i+2)
            break