i = 0
def solve(n):
    x = ""
    s = ""
    global i
    tem = 1
    while i < len(n):
        if x != "":
            tem = int(x)
        if n[i] == '[':
            i = i + 1
            #print(x)
            #tem2 = solve(n)
            #print(tem2, x)
            s = s + solve(n)
            #print(res, i)
        elif n[i] == ']':
            #print(tem * s)
            #i = i + 1
            #print(tem * s, i)
            return tem * s
        else:
            if n[i] >= '0' and n[i] <= '9':
                x = x + n[i]
            else:
                s = s + n[i]
        i = i + 1
    return tem * s
n = input()
print(solve(n), end = "")