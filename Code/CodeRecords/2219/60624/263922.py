import math
def func3():
    target = int(input())
    peak = int(math.sqrt(target))
    def helper():
        i, j = 0, peak
        while i <= peak and j >= 0:
            sum = i * i + j * j
            if sum == target:
                return True
            elif sum < target:
                i += 1
            else:
                j -= 1
        return False
    print(helper())
    return
func3()