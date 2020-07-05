nums = list(map(int, input()[1:-1].split(",")))
i = 1
while 1:
    if not i in nums:
        print(i)
        break
    i += 1