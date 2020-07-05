def minSwapsCouples(row):
    n = len(row)
    map = [0] * n
    count = 0
    for i in range(n):
        map[row[i]] = i
    for i in range(n):
        if row[i] % 2 == 0:  # 偶数 男生
            if (i != n-1 and row[i] + 1 == row[i + 1]) or (i != 0 and row[i] + 1 == row[i - 1]):
                continue
            else:
                row[map[row[i] + 1]] = row[i + 1]
                map[row[i + 1]] = map[row[i] + 1]
                row[i + 1] = row[i] + 1
                map[row[i] + 1] = map[row[i]] + 1
                count += 1
        else:  # 奇数 女生
            if (i != n - 1 and row[i] - 1 == row[i + 1]) or (i != 0 and row[i] - 1 == row[i - 1]):
                continue
            else:
                row[map[row[i] - 1]] = row[i + 1]
                map[row[i + 1]] = map[row[i] - 1]
                row[i + 1] = row[i] - 1
                map[row[i] - 1] = map[row[i]] + 1
                count += 1
    return count

if __name__ == "__main__":
    data = [int(a) for a in input().strip("[]").split(", ")]
    re = minSwapsCouples(data)
    print(re)