n=int(input())
for p in range(n):
    s = str(input())
    ss =[]
    res = ""
    for i in range(len(s)):
        if s[i] == "(":
            ss.append(s[i])
        elif s[i] == "+" or s[i] == "-":
            if len(ss) > 0:
                while not ss[len(ss) - 1] == "(":
                    res = res + ss[len(ss) - 1]
                    ss.pop()
                    if ss==[]:
                        break
                ss.append(s[i])
            else:
                ss.append(s[i])
        elif s[i] == "*" or s[i] == "/":
            if len(ss) > 0:
                while  ss[len(ss) - 1] == "*" or ss[len(ss) - 1] == "/" or ss[len(ss)-1]=="^":
                    res = res + ss[len(ss) - 1]
                    ss.pop()
                    if ss==[]:
                        break
                ss.append(s[i])
            else:
                ss.append(s[i])
        elif s[i]=="^":
            ss.append(s[i])
        elif s[i] == ")":
            while not ss[len(ss) - 1] == "(":
                res = res + ss[len(ss) - 1]
                ss.pop()
            ss.pop()
        else:
            res = res + s[i]
    if len(ss) > 0:
        res = res + ss.pop()
    print(res)