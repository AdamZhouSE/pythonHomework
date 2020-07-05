T = eval(input())
for i in range(T):
    nums = [int(x) for x in input().split()]
    N = eval(input())
    a1, a2 = nums
    gap = a2 - a1
    print(a1+(N-1)*gap)