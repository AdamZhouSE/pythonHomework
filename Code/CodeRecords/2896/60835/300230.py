s1 = list(input())
s2 = list(input())
res = "YES"
while len(s2) > 0:
    if s2[0] == ' ':
        del s2[0]
    else:
        if s2[0] not in s1:
            res = "NO"
            break
        else:
            del s2[0]
print(res, end = "")
