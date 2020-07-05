nums = eval(input())
i = 1
while True:
    try:
        ind = nums.index(i)
        i += 1
    except Exception:
        print(i)
        break
