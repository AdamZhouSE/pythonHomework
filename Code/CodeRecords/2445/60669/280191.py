def check(s,t):
    if len(s)!=len(t):
        return "false"
    else:
        arr = list(s)
        arr.sort()
        s = "".join(arr)
        arr = list(t)
        arr.sort()
        t = "".join(arr)
        for i in range(0, len(s)):
            if s[i]!=t[i]:
                return "false"
        return "true"


if __name__ == '__main__':
    string=input()
    s=eval(string.split(",")[0].split("=")[1].strip())
    t=eval(string.split(",")[1].split("=")[1].strip())
    print(check(s,t))