def test():
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    for i in range(N):
        if i+1 != nums[i]:
            B = nums[i]
            A = i+1
            break
    else:
        B = A = 0
    result.append('{:d} {:d}'.format(B, A))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)