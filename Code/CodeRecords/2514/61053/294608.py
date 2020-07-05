def isSubStr(s:str,t:str):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if t[j] == s[i]:
            i += 1
        j += 1
    return i == len(s)

if __name__ == "__main__":
    s = input()
    t = input()
    print(isSubStr(s,t))