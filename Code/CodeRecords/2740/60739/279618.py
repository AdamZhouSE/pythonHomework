def getInput():
    input_str = input();
    nums_str = input_str[1:len(input_str) - 1];
    nums = [str(n) for n in nums_str.split(",")];
    return nums;


def findMinDifference(timePoints):
    d = set()
    for c in timePoints:
        k = int(c[1: 3]) * 60 + int(c[4:6])
        if k in d:
            return 0
        d.add(k)
    d = sorted(d)
    d.append(d[0] + 1440)
    return min(d[i] - d[i - 1] for i in range(1, len(d)))

l = getInput()
print(findMinDifference(l))