def func14():
    s = input()
    t = input()
    flag = False
    for i in range(0, len(t)-len(s)+1):
        if flag:
            break
        cur = t[i:].find(s[0])
        if cur != -1:
            length = 1
            flag = True
            while length < len(s):
                cur = t[cur+1:].find(s[length])
                if cur == -1:
                    flag = False
                    break
                length += 1
        else:
            break
    print(flag)
    return
func14()