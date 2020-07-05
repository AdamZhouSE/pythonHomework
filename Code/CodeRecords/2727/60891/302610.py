t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    mice_l = [int(i) for i in input().split()]
    hole_l = [int(i) for i in input().split()]
    mice_l.sort()
    hole_l.sort()
    sum = 0
    for j in range(n):
        sum = max(sum,abs(hole_l[j] - mice_l[j]))
    ans_l.append(sum)
for i in ans_l:
    print(i)
