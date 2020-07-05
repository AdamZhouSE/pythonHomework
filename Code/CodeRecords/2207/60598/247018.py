times = int(input())
for i in range(times):
    cin = input().split(" ")
    A = int(cin[0])
    B = int(cin[1])
    Min = 0
    for j in range(1,1+B):
        Min += j
    if Min > A:
        print(0)
    else:
        print(1)
