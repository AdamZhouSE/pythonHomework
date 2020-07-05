def deal(s, t):
    ind = s.find(t)
    if (ind == -1):
        pass
    elif (ind == 0):
        s = s[len(t):]
    elif (ind == len(s) - len(t)):
        s = s[:len(s) - len(t)]
    else:
        s = s[:ind] + s[ind + len(t):]
    return s


s = input()
t = input()
while (True):
    if t in s:
        if (len(s) <= len(t)): break
        s = deal(s, t)
    else:
        break
print(s, end="")