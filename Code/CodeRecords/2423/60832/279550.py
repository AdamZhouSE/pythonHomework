All = int(input())

for q in range(0, All):
    temp = input().split()
    n1=int(temp[0])
    n2=int(temp[1])
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))

    isSub=True
    for x in ar2:
        if x not in ar1:
            isSub=False
            break
    
    if isSub:
        print("Yes")
    else:
        print("No")