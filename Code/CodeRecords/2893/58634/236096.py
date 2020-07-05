temp = input().replace("[","").replace("]","")
nums = [int(i) for i in temp.split(",")]
print((3 * sum(set(nums)) - sum(nums)) // 2)
