def factorial(n : int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
k = int(input())
res = ""
nums = list(range(1, n + 1))
turn = n - 1
rem = k - 1

while turn > 0:
    div = factorial(turn)
    index = rem // div
    res += str(nums[index])
    del nums[index]
    rem = rem % div
    turn -= 1
res += str(nums[0])
print(res)
