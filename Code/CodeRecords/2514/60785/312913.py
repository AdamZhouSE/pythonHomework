def isSubsequence(s, t):
    end = len(t)
    start = 0
    for i in s:
        if start >= end:
            return False
        if i not in t[start:end]:
            return False
        else:
            start = t.index(i, start, end) + 1
    return True
s=input("")
t=input("")
print(isSubsequence(s,t))