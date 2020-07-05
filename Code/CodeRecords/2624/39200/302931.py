s = input()
def cal(string):
    res = []
    for x in range(len(string)):
        if string[x] == "+" or string[x] == "-" or string[x] == "*":
            left = cal(string[0:x])
            right = cal(string[x+1:len(string)])
            for l in left:
                for r in right:
                    if string[x] == "+":
                        res.append(int(l) + int(r))
                    if string[x] == "-":
                        res.append(int(l) - int(r))
                    if string[x] == "*":
                        res.append(int(l) * int(r))
    if len(res) == 0:
        res.append(int(string))
    return res

print(cal(s))
