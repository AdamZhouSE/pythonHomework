def mysort( S, T):
    res = ""
    for char in S:
        res += char * T.count(char)
    for char in T:
            if char not in S:
                res += char
    return res
S=input("")
T=input("")
print(mysort(S,T))
