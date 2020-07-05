n = int(input())
if n < 3:
    print(n)
else:
    height = binary = [0]*n
    height[0] = 1
    Max = 0
    for i in range(n-1):
        li = input().split()
        parent = int(li[0])
        child = int(li[1])
        binary[parent] += 1
        if binary[parent] < 3:
            height[child] = height[parent] + 1
        Max = max(Max,height[child])
    print(Max)
