#12
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    even = []
    odd = []
    for item in num:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    if len(even) == 0:
        even = odd
    else:
        for item in odd:
            even.append(item)
    for j in range(0,n):
        print(even[j],end=" ")
    print("")