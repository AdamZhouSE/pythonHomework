m = int(input())
s = input()
for q in range(m):
    tem = input().split()
    if tem[0] == '1':
        s = s + tem[1]
        print(s)
    elif tem[0] == '2':
        s = s[int(tem[1]): int(tem[1]) + int(tem[2])]
        print(s)
    elif tem[0] == '3':
        n = int(tem[1])
        s = s[:n] + tem[2] + s[n:]
        print(s)
    elif tem[0] == '4':
        find = tem[1]
        cnt = 0
        #print(find, s)
        x = 0
        while x <(len(s) - len(find) + 1):
            if find == s[x: x + len(find)]:
                break
            else:
                x = x + 1
        if x == len(s) - len(find) + 1:
            x = -1
        print(x)