T = int(input())
for i in range(T):
    N = int(input())
    nums = input().split(' ')
    s = set()
    for j in nums:
        if j in s:
            s.remove(j)
        else:
            s.add(j)
    if s == set():
        print(0)
    else:
        print(s.pop())