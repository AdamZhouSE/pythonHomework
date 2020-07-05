

def solve():
    line = input().split(',')
    s = line[0][5:len(line[0]) - 1]
    t = line[1][6:len(line[1]) - 1]
    if len(s) != len(t):
        print('false')
        return
    for i in range(0,len(s)):
        if s[i] in t:
            index = t.index(s[i])
            if index == 0:
                t = t[1:]
            elif index == len(t) - 1:
                t = t[:index]
            else:
                t = t[:index] + t[index + 1:]
        else:
            print('false')
            return
    print('true')

solve()