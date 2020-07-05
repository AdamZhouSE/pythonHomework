def isSubsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)
s=input()
t=input()
if isSubsequence(s,t):print('True')
else:print('False')