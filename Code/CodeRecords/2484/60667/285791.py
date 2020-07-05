t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    length_a = li[0]
    length_b = li[1]
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    temp = n + m
    uni = []
    for j in temp:
        if j not in uni:
            uni.append(j)
    print(len(uni))        