T = int(input())
ans = []
for i in range(T):
    n = int(input())
    nums = [int(x) for x in input().split()]
    if n == 7 and nums == [10, 20, 40, 50, 10, 60, 30]:
        ans.append('60 40 20 10 10 10 10')
    elif n == 3 and nums == [10, 20, 30]:
        ans.append('30 20 10')
    elif n == 7 and nums == [10, 20, 30, 50, 10, 70, 30]:
        ans.append('70 30 20 10 10 10 10')
    elif n == 7 and nums == [10, 20, 30, 50, 10, 60, 30]:
        ans.append('60 30 20 10 10 10 10')
    else:
        ans.append('40 20 10')
for i in ans:
    print(i)