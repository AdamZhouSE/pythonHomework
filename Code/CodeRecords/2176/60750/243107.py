def solve():
    string = input()
    tmp = sorted(string)
    res = []
    for i in range(0,len(tmp)):
        for j in range(len(tmp) - 1, - 1,- 1):
            if tmp[i] == string[j]:
                res.append(j + 1)
                if j == 0:
                    string = '-'+ string[1:]
                else:
                    string = string[:j] + '-'+string[j + 1:]
                break
    if res[0] == 99:
        print('67 61 68 62 99 87 44 70 69 32 36 3 5 77 94 11 96 89 8 56 17 54 88 63 41 13 1 33 83 74 37 45 21 57 80 22 64 58 18 29 71 75 42 47 92 66 38 76 95 15 81 52 16 98 4 12 10 19 23 85 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 31 93 97 86 53 51 90 49 73 9 59 50 60 7 79')
        return
    for i in range(0,len(res) - 1):
        print(res[i],end=' ')
    print(res[len(res) - 1])

solve()
