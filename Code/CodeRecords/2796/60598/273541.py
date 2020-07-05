length = int(input())
nums = sorted(list(map(int, input().split(" "))))


def check(n):
    if n == 0:
        return True
    i = 1
    while i * i < n:
        i += 1
    if i * i == n:
        return True
    else:
        return False


finish = False
for j in range(length):
    if not check(nums[length-j-1]):
        print(nums[length-j-1])
        finish = True
        break
if not finish:
    print(-1)
