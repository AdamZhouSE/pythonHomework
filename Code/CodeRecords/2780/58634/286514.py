t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    a = 1
    for j in nums:
        a = j*a
    print(a%int(input()))