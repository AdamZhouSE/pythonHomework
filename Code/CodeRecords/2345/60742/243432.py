t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    count = [0]*n
    for i in a:
        count[i-1] += 1
    try:
        index1 = count.index(2)+1
    except ValueError:
        index1 = 0
    try:
        index2 = count.index(0)+1
    except ValueError:
        index2 = 0
    print(index1,index2)