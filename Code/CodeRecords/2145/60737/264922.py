t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    area = []
    for num in nums:
        area.append(num)
    for i in range(l-1):
        for j in range(i+2, l+1):
            wid = j-i
            hei = min(nums[i:j])
            area.append(wid*hei)
    maxi = max(area)
    print(maxi)
    t -= 1
    