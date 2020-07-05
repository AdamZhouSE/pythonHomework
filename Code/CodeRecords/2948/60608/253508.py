def func6():
    chars = list(input())
    base = eval(input())
    val = ""
    for item in chars:
        val += str(base + ord(item) - ord("A"))
    nums = list(val)
    while len(nums) > 2:
        if len(nums) == 3 and nums == ["1", "0", "0"]:
            break
        res = []
        for i in range(0, len(nums) - 1):
            res.append(str((int(nums[i]) + int(nums[i + 1])) % 10))
        nums = res[:]
    for i in range(0, len(nums) - 1):
        if nums[i] != "0":
            break
        else:
            del nums[i]
    print("".join(nums), end="")


func6()
