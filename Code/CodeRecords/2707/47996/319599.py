def minSwapsCouples(row):
    res = 0
    for i in range(0,len(row),2):
        tag = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
        if row[i + 1] != tag:
            tag_index = row.index(tag)
            row[i + 1], row[tag_index] = row[tag_index], row[i + 1]
            res += 1
    return res

nums = [int(x) for x in input()[1:-1].split(",")]
print(minSwapsCouples(nums))
