def cal(i):
    ds = []
    ori = i
    if i == 1:
        return 0
    else:
        x = 2
        while x < i + 1:
            if i % x == 0:
                ds.append(x)
                i /= x
                continue
            x += 1
        result = 0
        for d in ds:
            for char in str(d):
                result += int(char)
        temp = 0
        for char in str(ori):
            temp += int(char)
        if temp==result:
            return 1
        else:
            return 0

t = int(input())
for x in range(t):
    print(cal(int(input())))
