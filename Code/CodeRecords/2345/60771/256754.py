#44
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    num.sort()
    A = 0
    dup = []
    B = []
    for i in range(1,num[len(num)-1]):
        if i not in num:
            A = i
            break
    for item in num:
        if item not in dup:
            dup.append(item)
        else:
            B.append(item)
    if len(B) == 0:
        print(0,end=" ")
    else:
        B.sort()
        print(B[0],end=" ")
    print(A)
