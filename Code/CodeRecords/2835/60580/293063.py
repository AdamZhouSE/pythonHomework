size = int(input())
strList = input().split()
intList = []
for var in strList:
    intList.append(int(var))
d = {}
for var in intList:
    if var in d.keys():
        d[var] += 1
    else:
        d[var] = 1
if 0 not in d.keys():
    print(-1)
else:
    if 5 not in d.keys():
        print(0)
    else:
        x = 5
        while (x * d[x]) % 9 != 0:
            d[x] = d[x] - 1
            if d[x] <= 0:
                print(0)
                break
        if d[x] > 0:
            temp = ""
            for i in range(d[x]):
                temp += str(x)
            for i in range(d[0]):
                temp += str(0)
            print(temp)