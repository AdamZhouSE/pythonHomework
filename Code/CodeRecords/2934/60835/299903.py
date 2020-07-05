def solve(n):
    x = ""
    s = ""
    i = 0
    tem = 1
    while i < len(n):
        #print(s)
        if x != "":
            tem = int(x)
        if n[i] == '[':
            if s == "":
                res = solve(n[i + 1:len(n)])
                return tem* res
            else:
                res = solve(n[i + 1:len(n)])
                return tem * s + res
        elif n[i] == ']':
            return tem * s
        else:
            if n[i] >= '0' and n[i] <= '9':
                x = x + n[i]
            else:
                s = s + n[i]
        i = i + 1
    return tem* s
n = input()
print(solve(n))