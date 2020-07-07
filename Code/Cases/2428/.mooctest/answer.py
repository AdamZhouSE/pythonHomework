tc = int(input())
while tc:
    size = int(input())
    nums = list(map(int,input().split()))
    odd = []
    even = []
    for i in range(size):
        if nums[i]%2==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    odd.sort(reverse = True)
    even.sort()
    oddeven = odd + even
    for i in range(size):
        print(oddeven[i], end=" ")
    print()
    tc -= 1