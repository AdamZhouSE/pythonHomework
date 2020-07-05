from sys import stdin


def find_next_spec(n):
    t = ""
    if is_made_of_4(n):
        t = str(n)[0:len(str(n)) - 1]
        return int(t + '7')
    if is_made_of_7(n):
        for i in range(0, len(str(n) )+ 1):
            t += '4'
        return int(t)
    if str(n).endswith('4'):
        return int(str(n)[0:len(str(n)) - 1] + '7')
    else:
        index = find_last_4(str(n))
        t = str(n)[0:index-1 ] + '7'
        for j in range(0, len(str(n)) - index):
            t += '4'
        return int(t)


def find_last_4(str):
    s = list(str)
    s.reverse()
    count = 0
    while True:
        if s[count] == '4':
            return len(s)-count
        count += 1


def is_made_of_4(s):
    t = list(str(s))
    return t.count('4') == len(t)


def is_made_of_7(s):
    t = list(str(s))
    return t.count('7') == len(t)


num = int(stdin.readline().strip())
for i in range(0, num):
    a = int(stdin.readline().strip())
    start = 4
    for j in range(1, a):
        start = find_next_spec(start)      
    print(start)