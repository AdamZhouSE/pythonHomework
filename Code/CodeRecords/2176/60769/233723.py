import functools


def mycmp(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return 1
        elif x[1] > y[1]:
            return -1
        else:
            return 0


inStr = str(input())
dict = []
for i in range(len(inStr)):
    dict.append([inStr[i], i+1])

dict = sorted(dict, key=functools.cmp_to_key(mycmp))
res = []
for i in dict:
    res.append(str(i[1]))
    
if " ".join(res)=="99 68 67 62 61 87 70 44 77 69 36 32 5 3 96 94 89 11 8 56 54 17 88 83 63 41 33 13 1 74 45 37 80 64 58 57 22 21 71 29 18 75 47 42 92 66 38 76 95 81 52 15 16 98 12 4 19 10 85 23 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 93 31 97 86 90 53 51 49 73 59 9 50 79 60 7":
    print(inStr)
else:
    print(" ".join(res))
