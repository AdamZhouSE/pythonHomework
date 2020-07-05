import math
def func6():
    nums = list(map(int, input().split(",")))
    threshold = int(input())
    for i in range(threshold,0,-1):
        j = 0
        for num in nums:
            j += math.ceil(num/i)
        if j > threshold:
            print(i+1)
            break
    return
func6()