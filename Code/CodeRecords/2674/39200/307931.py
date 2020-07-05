import itertools

t = int(input())
for x in range(t):
    s = input()
    A = []
    B = []
    C = []
    for i in range(len(s)):
        if s[i] == "a":
            A.append(s[i])
        elif s[i] == "b":
            B.append(s[i])
        elif s[i] == "c":
            C.append(s[i])
    lst = []
    for i in range(3, len(s) + 1):
        lst.extend([''.join(a) for a in itertools.combinations(s, i)])
    #print(s)
    #print(lst)
    count = 0
    for i in lst:
        state = 0
        flag = 1
        for a in i:
            if i[0] != "a" or i[len(i) - 1] != "c":
                flag = 0
                break
            if a == "a" and state != 0:
                flag = 0
                break
            elif a == "b" and state == 2:
                flag = 0
                break
            elif a == "b":
                state = 1
            elif a == "c" and state == 0:
                flag = 0
            elif a == "c":
                state = 2
        if flag:
            count += 1
    print(count)
