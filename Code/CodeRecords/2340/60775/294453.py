def cal(n,height:list):
    if n <=2:
        return 0

    first = 0
    end = first + 1
    last = first + 1
    water = 0
    while first < n - 1:
        for last in range(first+1,n):
            if height[last] >= height[first]:
                end = last
                break
            elif height[end] < height[last] < height[first]:
                end = last
                continue
        shorter = min(height[first],height[end])
        tmp = 0
        for idx in range(first+1,end):
            tmp += shorter-height[idx]
        water += tmp
        first = end
        end += 1
    return water

T = int(input())

for t in range(T):
    n = int(input())
    height = [int(x) for x in input().split(' ')]
    print(cal(n,height))
